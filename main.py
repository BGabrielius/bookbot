def main():
    print("--- Begin report of books/frankenstein.txt ---")
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        count_words_from_file(file_contents)
        count_chart(file_contents)
    print("--- End report ---")
        
def count_words_from_file(file_contents):
    words = file_contents.split()
    print(f"{len(words)} words found in the document")
    return len(words)

def count_chart(file_contents):
    chart_count = {}
 
    for chart in file_contents.lower():
        if chart in chart_count:
            chart_count[chart] += 1
        else:
            chart_count[chart] = 1
    return convert_to_sorted_list(chart_count)

def convert_to_sorted_list(dict):
    list_of_dict = []
    for chart in dict:
        if chart.isalpha():
            chart_dict = {"chart": chart, "count": dict[chart]}
            list_of_dict.append(chart_dict)
        else:
            continue
    list_of_dict.sort(reverse=True, key=sort_on)
    return print_chart_report(list_of_dict)

def sort_on(dict):
    return dict["count"]

def print_chart_report(list_of_dict):
    print(" ")
    print(" ")
    for dict in list_of_dict:
        print(f"The '{dict["chart"]}' character was found {dict["count"]} times")


main()

