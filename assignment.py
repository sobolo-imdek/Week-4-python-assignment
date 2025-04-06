# File Read and Write Challenge

def read_and_modify_file(input_filename, output_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
        
        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()  # You can modify this as needed
        
        # Open the output file in write mode
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
        
        print(f"Modified content has been written to {output_filename}")
    
    except FileNotFoundError:
        print(f"The file {input_filename} does not exist.")
    except IOError as e:
        print(f"Error occurred: {e}")

# Usage example:
input_filename = 'input.txt'
output_filename = 'output.txt'
read_and_modify_file(input_filename, output_filename)
