def preprocess_file(content):
    append_subcollections(content)

    # Format lists.
    

    return content

def append_subcollections(content):
    include_index = content.find("<!-- include:files")
    while include_index != -1:
        include_block = content[include_index:content.find("-->", include_index) + 3]
        
        if "\n" in include_block:
            break

        path_index = include_block.find("path=\"")
        if path_index != -1:
            path = include_block[path_index + 6:include_block.find("\"", path_index + 6)]
            
            strat_index = include_block.find("insert=\"")
            if strat_index != -1:
                strat = include_block[strat_index + 8:include_block.find("\"", strat_index + 8)]
            else:
                strat = ""

            match strat:
                case "h-table":
                    pass
                case "table":
                    pass

        include_index = content.find("<!-- include:files", include_index + 1)