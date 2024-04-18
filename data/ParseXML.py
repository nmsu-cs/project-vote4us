import os
import xml.etree.ElementTree as ET

def extract_coordinates(xml_file_path, output_file_path):
    for xml_file_name in os.listdir(xml_file_path):
        if xml_file_name.endswith('.xml'):
            print(xml_file_name)
            
            full_xml_file_path = os.path.join(xml_file_path, xml_file_name)
            print (full_xml_file_path)

            file_id = xml_file_name.split('.')[0] if '.' in xml_file_name else xml_file_name
            # Extract YOLO format values
            
            
            
            # Parse the XML file
            tree = ET.parse(full_xml_file_path)
            root = tree.getroot()

            output_file_path = os.path.join(xml_file_path, file_id)

            # Find 'bndbox' element under 'object'
            bndbox = root.find('object/bndbox')
    
            # Extract coordinates
            size_width = int(root.find('size/width').text)
            size_height = int(root.find('size/height').text)
            xmin = int(bndbox.find('xmin').text)
            ymin = int(bndbox.find('ymin').text)
            xmax = int(bndbox.find('xmax').text)
            ymax = int(bndbox.find('ymax').text)

            # Calculate box width and height
            box_width = xmax - xmin
            box_height = ymax - ymin
    
            # Calculate box center coordinates
            x_center = xmin + (box_width / 2)
            y_center = ymin + (box_height / 2)
    
            # Normalize coordinates and dimensions
            x_center /= size_width
            y_center /= size_height
            box_width /= size_width
            box_height /= size_height

            #output_file_path = r'C:\Users\theti\OneDrive\Desktop\School Suff\S4\CS371\Waldo_Project\WSG_Waldo\project-vote4us\data\labels\train'
            # Write YOLO format values to output file
            with open(output_file_path, 'w') as f:
                f.write(f"0 {x_center} {y_center} {box_width} {box_height}\n")

            print(f"Processed {xml_file_name} and saved to {output_file_path}")
    
    # done
    print("finished parsing")
    
    

# Path to the XML file
xml_file_path = r"C:\Users\theti\OneDrive\Desktop\School Suff\S4\CS371\Waldo_Project\WSG_Waldo\project-vote4us\data\labels\trainxml"
output_file_path = r'C:\Users\theti\OneDrive\Desktop\School Suff\S4\CS371\Waldo_Project\WSG_Waldo\project-vote4us\data\labels\train'

# Convert to YOLO format
extract_coordinates(xml_file_path, output_file_path)


