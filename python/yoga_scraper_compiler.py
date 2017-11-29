yoga_dict = {'Radiant Health Yoga Teacher Training Program': (
    'https://www.yogaalliance.org/SchoolPublicProfile?sid=1188&lid=1188', 'Bend, OR, USA  map'), 'Eugene Yoga': (
    'https://www.yogaalliance.org/SchoolPublicProfile?sid=2351&lid=8551',
    '3575 Donald Street\nEugene, OR, United States  map'), 'DAYA Foundation': (
    'https://www.yogaalliance.org/SchoolPublicProfile?sid=2336&lid=2336', 'Portland, OR 97239, USA  map'),
    'School Yoga Institute Ashland Oregon': (
        'https://www.yogaalliance.org/SchoolPublicProfile?sid=359&lid=359',
        '585 Weller Lane\nAshland, OR, USA  map'), 'The Movement Center, Inc.': (
        'https://www.yogaalliance.org/SchoolPublicProfile?sid=2269&lid=2269', 'Portland, OR 97232, USA  map'),
    'CorePower Yoga (Northwest Portland)': (
        'https://www.yogaalliance.org/SchoolPublicProfile?sid=1152&lid=3898',
        '2277 Northwest Quimby Street\nPortland, OR 97210, USA  map'), 'CorePower Yoga (Bridgeport Village)': (
        'https://www.yogaalliance.org/SchoolPublicProfile?sid=1152&lid=9804',
        '7497 Southwest Bridgeport Road\nPortland, OR, United States  map'), 'CorePower Yoga (Southeast Portland)': (
        'https://www.yogaalliance.org/SchoolPublicProfile?sid=1152&lid=9805',
        '844 Southeast Morrison Street\nPortland, OR, United States  map'), 'The Lotus Seed': (
        'https://www.yogaalliance.org/SchoolPublicProfile?sid=2743&lid=2743', 'Portland, OR 97212, United States  map'),
    'Asmi Yoga': ('https://www.yogaalliance.org/SchoolPublicProfile?sid=715&lid=715', 'Bend, OR, USA  map')}

for i in yoga_dict.keys():
    temp_val = yoga_dict[i][-1]
    # yoga_dict[i].remove(temp_val)
    temp_val = temp_val[:-5]
    print(temp_val)
    print(type(temp_val))
    print(temp_val)
    yoga_dict[i].append(temp_val)
    print(yoga_dict[i])

