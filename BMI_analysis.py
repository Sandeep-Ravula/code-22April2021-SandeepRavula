from pprint import pprint
import json

def BMI(gender,height,weight):
    """
    This function will calculates the BMI rate of each sample and returns the output data
    :param gender: indicates gender of the person to be BMI analysed
    :param height: indicates height in metres
    :param weight: indicates weight in kgs
    :return: a tuple of gender,height,weight,bmi,bmi_category,health_risk
    """
    bmi_index_limits=[18.4,24.9,29.9,34.9,39.9,40.0]
    bmi_categories=["Underweight", "Normal weight", "Overweight", "Moderately obese", "Severely obese", "Very severely obese"]
    health_risk=["Malnutrition risk", "Low risk", "Enhanced risk", "Medium risk", "High risk",
"Very high risk"]

    bmi=weight/(height**2)                ##  BMI formula : BMI(kg/m**2) = mass(kg) / height(m**2)

    if bmi <= bmi_index_limits[0]:
        return (gender,height,weight, bmi,bmi_categories[0],health_risk[0])
    elif bmi_index_limits[0] < bmi <= bmi_index_limits[1]:
        return (gender,height,weight,bmi, bmi_categories[1], health_risk[1])
    elif bmi_index_limits[1] < bmi <= bmi_index_limits[2]:
        return (gender,height,weight,bmi, bmi_categories[2], health_risk[2])
    elif bmi_index_limits[2] < bmi <= bmi_index_limits[3]:
        return (gender,height,weight,bmi, bmi_categories[3], health_risk[3])
    elif bmi_index_limits[3] < bmi <= bmi_index_limits[4]:
        return (gender,height,weight,bmi, bmi_categories[4], health_risk[4])
    elif bmi >= bmi_index_limits[5]:
        return (gender,height,weight,bmi, bmi_categories[5], health_risk[5])


def get_Count_of_overWeight_ppl(consolidated_data):
    """
    It will return the count of number of overweighted people among the given input samples

    :param consolidated_data: (list)
    :return: count_overweight (int)
    """
    count_overweight=0
    for data in consolidated_data:
        if data[4]=='Overweight':
            count_overweight+=1
    return count_overweight


def main(input_file):
    """
    This

    :param input_file: Input file containing given JSON data

    """
    output_list=[]
    data_file=open(input_file,'r')
    json_data=json.load(data_file)
    for bmi_data in json_data:
        response=BMI(bmi_data['Gender'],bmi_data['HeightCm']/100,bmi_data['WeightKg'])
        output_list.append(response)
        print(response)

    count_overweight_ppl=get_Count_of_overWeight_ppl(output_list)
    overweight_percent=count_overweight_ppl/len(output_list)*100
    print('\n\ncount of overweight people is:',count_overweight_ppl)
    print(f'\nMy observation: out of total BMI samples, {round(overweight_percent,2)} % are overweighted')
    

main('BMI_analysis_JSON_data.json')


