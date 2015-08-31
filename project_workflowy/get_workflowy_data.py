import requests

def get_response_data(page_id):
	page_url = "https://workflowy.com/get_initialization_data?share_id=%s&client_version=14" %page_id
	response = requests.get(page_url)
	if not response.ok:
		print('response not ok')
		return None

	data = response.json()
	return(data)

""" UTILITY FUNCTIONS """

def get_root_data(data):
	root_data = data["projectTreeData"]["mainProjectTreeInfo"]
	return root_data

def get_root_name(data):
	name = data["rootProject"]["nm"]
	return name

""" UTILITY FUNCTIONS END """

""" CASE SPECIFIC """

def parse_quote_data(response_data):
	""" a case specific function that parses data for the project 'quotes' """
	data = get_root_data(response_data)

	return_data = []
	root_children = data["rootProjectChildren"]
	for child in root_children:
		quote = child["nm"]
		source = child["ch"][0]["nm"]
		return_data.append({"quote":quote, "source":source})
	return return_data

def parse_topic_data(response_data):
	""" a case specific function that parses the data for the project 'core_competencies' """
	data = get_root_data(response_data)

	return_data = []
	root_children = data["rootProjectChildren"]
	for child in root_children:
		child_data = {}
		title = str(child["nm"])
		subtitles = child.get("ch", [])
		subtitles_data = []
		for subtitle in subtitles:
			subtitle_data = {}
			subtitle_name = str(subtitle["nm"])

			subtitle_children = subtitle.get("ch", [])
			subtitle_children_content = []
			for content in subtitle_children:
				content_data = str(content["nm"])
				if not content.get("ch", []):
					subtitle_children_content.append(content_data)
				else:
					subtitle_children_content.append({"data":content_data, "value":content["ch"][0]["nm"]})

			subtitle_data["name"] = subtitle_name
			subtitle_data["content"] = subtitle_children_content

			subtitles_data.append(subtitle_data)

		child_data = {
			"name":title,
			"content":subtitles_data
		}

		return_data.append(child_data)

	return return_data

""" CASE SPECIFIC END """

