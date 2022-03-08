
# Library used for string matching 
import re
# Library for dealing with arrays, (similar to matlab) 
import pandas as pd 


# TODO: Replace this with your file
raw_text = '''LINEAR X 5.218560 Y 55.569300 Z 15.481700 PH 0.000000 RH 18.949000 RZ 5.218560 F30.00
CALL Extruder(23.25115)
LINEAR X -4.176620 Y 55.518900 Z 15.619600 PH 0.000000 RH 18.861500 RZ -4.176620 F30.00
LINEAR X -4.350420 Y 55.438300 Z 15.840700 PH 0.000000 RH 18.721000 RZ -4.350420 F130.00
CALL Extruder(28.73532)
LINEAR X -3.719350 Y 62.022100 Z -0.916121 PH 0.000000 RH 28.894000 RZ -3.719350 F30.00
CALL Extruder(34.21955)
LINEAR X 4.602550 Y 62.081000 Z -1.057290 PH 0.000000 RH 28.976300 RZ 4.602550 F30.00
CALL Extruder(39.70373)
LINEAR X 5.382000 Y 55.489600 Z 15.699800 PH 0.000000 RH 18.810600 RZ 5.382000 F30.00
CALL Extruder(45.18083)
LINEAR X -4.337820 Y 55.437700 Z 15.842300 PH 0.000000 RH 18.720000 RZ -4.337820 F30.00
LINEAR X -4.495650 Y 55.370500 Z 16.027100 PH 0.000000 RH 18.602400 RZ -4.495650 F130.00
CALL Extruder(45.20496)
LINEAR X -4.507220 Y 55.394500 Z 15.961000 PH 0.000000 RH 18.644500 RZ -4.507220 F30.00
CALL Extruder(50.78725)
LINEAR X -3.842710 Y 62.097900 Z -1.097820 PH 0.000000 RH 29.000000 RZ -3.842710 F30.00
CALL Extruder(50.81137)
LINEAR X -3.827850 Y 62.128600 Z -1.171480 PH 0.000000 RH 29.042900 RZ -3.827850 F30.00
CALL Extruder(50.84972)
LINEAR X -3.772190 Y 62.143400 Z -1.207030 PH 0.000000 RH 29.063600 RZ -3.772190 F30.00
CALL Extruder(56.41495)
LINEAR X 4.653290 Y 62.203300 Z -1.350400 PH 0.000000 RH 29.147100 RZ 4.653290 F30.00
CALL Extruder(56.45330)
LINEAR X 4.709130 Y 62.189200 Z -1.316690 PH 0.000000 RH 29.127400 RZ 4.709130 F30.00
CALL Extruder(56.47742)
LINEAR X 4.724480 Y 62.158600 Z -1.243430 PH 0.000000 RH 29.084800 RZ 4.724480 F30.00
CALL Extruder(62.05971)
LINEAR X 5.539880 Y 55.447400 Z 15.815700 PH 0.000000 RH 18.736900 RZ 5.539880 F30.00
CALL Extruder(62.08384)
LINEAR X 5.529080 Y 55.423200 Z 15.882200 PH 0.000000 RH 18.694600 RZ 5.529080 F30.00
CALL Extruder(62.12218)
LINEAR X 5.467710 Y 55.406200 Z 15.928900 PH 0.000000 RH 18.664900 RZ 5.467710 F30.00
CALL Extruder(67.68741)
LINEAR X -4.433670 Y 55.354200 Z 16.072000 PH 0.000000 RH 18.573800 RZ -4.433670 F30.00
CALL Extruder(67.71863)
LINEAR X -4.484210 Y 55.367400 Z 16.035600 PH 0.000000 RH 18.597000 RZ -4.484210 F30.00
LINEAR X -4.480250 Y 55.393600 Z 15.963400 PH 0.000000 RH 18.642900 RZ -4.480250 F130.00
CALL Extruder(65.71863)
LINEAR X -4.480250 Y 55.393600 Z 15.963400 PH 0.000000 RH 18.642900 RZ -4.480250 F40.00
CALL Extruder(0.00000)
LINEAR X -3.975070 Y 55.564500 Z 15.494900 PH 0.000000 RH 18.940700 RZ -3.975070 F130.00
CALL Extruder(2.00000)
LINEAR X -3.975070 Y 55.564500 Z 15.494900 PH 0.000000 RH 18.940700 RZ -3.975070 F40.00
CALL Extruder(2.09416)
LINEAR X -4.082960 Y 55.638100 Z 15.293800 PH 0.000000 RH 19.068200 RZ -4.082960 F30.00
CALL Extruder(2.21633)
LINEAR X -4.067820 Y 55.764700 Z 14.948600 PH 0.000000 RH 19.286700 RZ -4.067820 F30.00
'''

# split text file into array
raw_text_lines = raw_text.splitlines()

# merge lines with LINEAR and CALL into one line. Note this input array will need to have an even number. 
def merge_every_second_line(raw_text_lines):
    res = []
    for idx in range(0, len(raw_text_lines), 2):
        res.append(f'{raw_text_lines[idx]} \n {raw_text_lines[idx+1]}')   # you will have to ensure the number of elements is even, or protect against an Indexerror
    
    return res
    
# Call the function above to merge the lines into 1, this makes life easier in the next step.
raw_text_lines = merge_every_second_line(raw_text_lines)

# Create an empty array to put the values in
cordinates_list = []

p = re.compile(r'\d+\.\d+')  # Compile a pattern to capture float values

# Loop through every line 
for raw_text_line in raw_text_lines:

    # Extract all numbers from string 
    cordinates = [float(i) for i in p.findall(raw_text_line)]  

    # Add them cordinates to the list
    cordinates_list.append(cordinates)

    # TODO: If you wanted at this stage you could edit the previous line to put the values into a dict

# Sanity check: Print the first three values of the array
first_three = str(cordinates_list[0:3])
print(first_three)

# Convert the python array of arrays into a 2D array
cordinates_df = pd.DataFrame(cordinates_list)

cordinates_df.to_csv(r'results.csv')
cordinates_df.to_excel(r'results.xlsx')

print('done')
