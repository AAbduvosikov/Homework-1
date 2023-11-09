from django.shortcuts import render


def main(request):
    print(request,"request ma'lumotlari")
    context ={'content':[
        {'Name':'Nexia','Year':'2020','Price':'9500','Color':'White'},
        {'Name':'Malibu','Year':'2023','Price':'15600','Color':'Black'},
        {'Name':'Gentra','Year':'2013','Price':'8200','Color':'White'},
        {'Name':'Damas','Year':'2015','Price':'5900','Color':'White'},
        {'Name':'Matiz','Year':'2011','Price':'2999','Color':'Black'},
        {'Name':'Spark','Year':'2009','Price':'3599','Color':'Blue'},
        {'Name':'Epica','Year':'2008','Price':'5999','Color':'Yellow'},

    ]}
    return render(request,'main.html',context)

