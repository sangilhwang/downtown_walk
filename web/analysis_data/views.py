from django.shortcuts import render
from analysis_data.models import DistrictData


# Create your views here.
def analysisplot(request):
    keyword = request.GET.get("keyword", None)
    keyword1 = request.GET.get("keyword1", None)

    if keyword: #keyword값이 주어진 경우
    # 선택으로 전달받은 키워드 값으로 정렬순서 및 value1 수정
        district = DistrictData.objects.all().order_by(keyword)

        # x축의 자치구 이름 리스트
        xlabels = [item["district_name"] for item in district.values()]
        # y1의 상가유형에 따른 임대료 리스트
        values1 = [item[keyword] for item in district.values()]

        # values1의 상가유형
        if keyword == 'large_b1_rent':
            labels1 = ["중대형 지하 1층"]
        elif keyword == 'large_1_rent':
            labels1 = ["중대형 1층"]
        elif keyword == 'large_2_rent':
            labels1 = ["중대형 2층"]
        elif keyword == 'large_3_rent':
            labels1 = ["중대형 3층"]
        elif keyword == 'large_4_rent':
            labels1 = ["중대형 4층"]
        elif keyword == 'large_5_rent':
            labels1 = ["중대형 5층"]
        elif keyword == 'large_6to10_rent':
            labels1 = ["중대형 6~10층"]
        elif keyword == 'small_b1_rent':
            labels1 = ["소형 지하 1층"]
        elif keyword == 'small_1_rent':
            labels1 = ["소형 1층"]
        else:
            labels1 = ["소형 2층"]

        # compare1의 비교데이터 유형 및 비교데이터
        if keyword1 == 'employee_density':
            labels2 = ["종사자밀도"]
            compare1 = []
            for i in district:
                compare1.append(i.employeedata_set.all().values()[0][keyword1])
        elif keyword1 == 'employee_ratio':
            labels2 = ["종사자/거주인구"]
            compare1 = []
            for i in district:
                compare1.append(i.employeedata_set.all().values()[0][keyword1])
        elif keyword1 == 'total_ratio':
            labels2 = ["유동인구/면적"]
            compare1 = []
            for i in district:
                compare1.append(i.floatpopdata_set.all().values()[0][keyword1])
        elif keyword1 == 'ratio_30s':
            labels2 = ["30대 인구/면적"]
            compare1 = []
            for i in district:
                compare1.append(i.seoulpopdata_set.all().values()[0][keyword1])
        elif keyword1 == 'ratio_40s':
            labels2 = ["40대 인구/면적"]
            compare1 = []
            for i in district:
                compare1.append(i.seoulpopdata_set.all().values()[0][keyword1])
        else:
            labels2 = ["50대 인구/면적"]
            compare1 = []
            for i in district:
                compare1.append(i.seoulpopdata_set.all().values()[0][keyword1])

    else:  # keyword가 주어지지 않아, None이 할당된 경우

        # 초기값으로 중대형 1층을 기준으로 정렬
        district = DistrictData.objects.all().order_by('large_1_rent')

        # 중대형 1층에 대하여 종사자밀도와 데이터 비교
        labels1 = ["중대형 1층"]
        labels2 = ["종사자밀도"]
        xlabels = [item.district_name for item in district]
        values1 = [item.large_1_rent for item in district]
        compare1 = []
        for i in district:
            compare1.append(i.employeedata_set.all().values()[0]['employee_density'])

    context = {
        "labels1" : labels1,
        "labels2" : labels2,
        "xlabels" : xlabels,
        "values1" : values1,
        "compare1" : compare1,
        }
    return render(request, "analysis_page.html", context)
