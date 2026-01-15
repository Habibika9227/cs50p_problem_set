def main():
    item_list=[]
    while True:
        try:
            items=input().upper()
            item_list.append(items)
        except EOFError:
            print()
            break
    result=frequency(item_list)    
    for item in sorted(result):
        print(result[item],item)
    

def frequency(par):
    item_dic={}
    for items in par:
        if items in item_dic:
            item_dic[items]+=1
        else:
            item_dic[items]=1
    
    return item_dic

main()