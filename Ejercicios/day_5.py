
#1
c1 = []
print(type(c1))

#2
c2 = [1, 2, 3, 4, "Cinco"]
print(c2)

#3
c3 = [1, 2, 3, 4, "Cinco"]
print(len(c3))

#4
c4 = [1, 2, 3, 4, "Cinco"]
print(c3[0],c3[2],c3[4])

#5
mixed_data_types = ["Brandon", 25, 71, "Single", "Vallarta 5846" ]
print(mixed_data_types)

#6
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon" ]

#7
print(it_companies)

#8
print(len(it_companies))

#9
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon" ]
print(it_companies[0],it_companies[3],it_companies[-1])

#10
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon" ]
it_companies.insert(2,"Chachitos")
print(it_companies)

#11
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon" ]
it_companies.append("Tesla")
print(it_companies)

#12
it_companies.insert(4,"BMW")
print(it_companies)

#13
c13 = it_companies.pop(2)
c13 = c13.upper()
it_companies.insert(2,c13)
print(it_companies)

#14
c14 = " # ".join(it_companies)
print(c14)

#15
c15 = "BMW" in it_companies
print(c15)

#16
c16 = it_companies[2:6]
print(c16)

#17
it_companies.reverse()
print(it_companies)

#18
c18 = it_companies[0:3]
print(c18)

#19

c19 = it_companies[-3:]
print(c19)

#20
c20 = int((len(it_companies)-1)/2)
c20n = it_companies[c20]
print(c20n)

#21
print(it_companies)
it_companies.pop(0)
print(it_companies)

#22
c22 = int((len(it_companies)-1)/2)
it_companies.pop(c22)
print(it_companies)

#23
it_companies.pop()
print(it_companies)

#24
it_companies.clear()
print(it_companies)

#25
del it_companies
#print(it_companies)

#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
join_list = front_end + back_end
print(join_list)

#27
full_stack = join_list
full_stack.insert(full_stack.index("Redux")+1,"Python")
full_stack.insert(full_stack.index("Python")+1,"SQL")
print(full_stack)

full_stack.insert("")
full_stack.insert()
print(full_stack)


### Exercises: Level 2 ###

#0
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(ages)
ages.sort()
e_min = min(ages)
e_max = max(ages)
print(f"La edad mas baja es {e_min} y la edad mas alta es {e_max}")
ages.append(e_max)
ages.insert(0,e_min)
print(ages)
e_int = int((len(ages))/2)
e_med = int((ages[e_int] + ages[e_int + 1]) / 2)
print(e_med)
e_prom = sum(ages)/len(ages)
print(e_prom)
e_range = e_max - e_min
print(e_range)
abs_min = abs(e_min - e_prom)
abs_max = abs(e_max - e_prom)
print(abs_min)
print(abs_max)

#193 paises 

countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombi', 'Comoros', 'Congo (Brazzaville)', 'Congo', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor (Timor Timur)', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 'Korea, South', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia and Montenegro', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']
#1
e1_len = len(countries)
print(countries)
if e1_len%2 == 0:
    print("Es par")
    e1_int = int((len(countries))/2)
    e1_med = countries[e1_int], countries[e1_int + 1]
    print(e1_med)
else:
    e1_med = countries[int((len(countries))/2) + 1]    
    print(e1_med)

#2
e1_len = len(countries)
if e1_len%2 == 0:
    print("Es par")
    e1_int = int((len(countries))/2)
    e1_mit1 = countries[0:(e1_int+1)]
    e1_mit2 = countries[(e1_int+1):-1]
    print(e1_mit1)
    print(e1_mit2)

else:
    e1_int = int((len(countries))/2)
    e1_mit1 = countries[0:(e1_int+2)]
    e1_mit2 = countries[(e1_int+2):-1]
    print(e1_mit1)
    print(e1_mit2)

#3
little_list = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
e3 = little_list[:3]
e3_scandic = little_list[3:]
print(f"Primeros tres paises {e3}")
print(f"Paises escandinavos {e3_scandic}")

little_list = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']


