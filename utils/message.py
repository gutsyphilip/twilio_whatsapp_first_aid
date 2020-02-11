
def convert_result_to_message(result):
    if len(result) == 0:
        return "Sorry, we currently don't have any data pertaining to your ailment"
    message = ""
    for data in result:
        message += f"Ailment: {data['injury']}\n"
        message += f"Treatment: {data['treatment']}\n\n"
    return message