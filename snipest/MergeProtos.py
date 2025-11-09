import os , glob
from google.protobuf import descriptor_pb2
from google.protobuf import text_format
from proto_schema_parser.parser import Parser
import proto_schema_parser
from proto_schema_parser.generator import Generator


# Path to the root folder containing all .proto files
PROTO_ROOT = "defold-sdk"
OUTPUT_FILE = "merged.proto"

class MergeProtos : 
    def __init__(self,folder,export = "Merged.proto") : 
        self.protos = folder
        self.syntax='proto3'
        files = self.get_all_proto_files()
        elements = list()
        for file in files : 
            x = self.parseFile(file)
            elements.extend(x)
        self.cleanElements(elements) 
        Mergedfile = proto_schema_parser.ast.File(syntax='proto3' , file_elements  = elements)
        proto = Generator().generate(Mergedfile)
        print(proto , file = open(export , "w"))

    def get_all_proto_files(self):
        root_folder = self.protos
        proto_files = []
        for dirpath, _, filenames in os.walk(root_folder):
            for file in filenames:
                if file.endswith(".proto"):
                    full_path = os.path.join(dirpath, file)
                    proto_files.append(full_path)
        return proto_files

    def parseFile(self,file) : 
        result = []
        parser = Parser()
        res = parser.parse(open(file).read())
        self.syntax = res.syntax
        for e in res.file_elements : 
            new_el = None 
            if type(e).__name__ == "Message" : 
                msg = type(e)(name = e.name)
                for el_index , el in enumerate(e.elements) : 
                    if type(el).__name__ == "Field" : 
                        msg.elements.append(el)
                result.append(msg)
            if type(e).__name__ == "Enum" : 
                enum = type(e)(name = e.name)
                for el in e.elements : 
                    if type(el).__name__ == "EnumValue" : 
                        enum.elements.append(el)
                result.append(enum)
        return result

    def cleanElements(self,elements) : 
        for i , e in enumerate(elements) : 
            if type(e).__name__ == "Message" : 
                for fi ,  f in enumerate(e.elements) : 
                    #elements[i].elements[fi].type = f.type.split(".")[-1]
                    for opi , op in enumerate(f.options) : 
                        if self.is_uint32_hex(op.value) : 
                            elements[i].elements[fi].options[opi].value = self.hex_to_uint32(op.value)

                    pass 

                

    def is_uint32_hex(self,value):
        """
        Check if a value represents a uint32 in hexadecimal format.
        Accepts strings like "0xffffffff" or integers.
        """
        if isinstance(value, str):
            # Check if it starts with 0x and is a valid hex number
            try:
                n = int(value, 16)
                return 0 <= n <= 0xFFFFFFFF
            except ValueError:
                return False
        elif isinstance(value, int):
            # Check if integer is within uint32 range
            return 0 <= value <= 0xFFFFFFFF
        else:
            return False

    def hex_to_uint32(self,value):
        """
        Convert a hex string or integer to uint32 (0 - 0xFFFFFFFF)
        """
        if isinstance(value, str):
            # Convert string to int
            if value.lower().startswith("0x"):
                n = int(value, 16)
            else:
                n = int(value)
        elif isinstance(value, int):
            n = value
        else:
            raise ValueError("Value must be int or string")

        # Ensure it's in uint32 range
        if not (0 <= n <= 0xFFFFFFFF):
            raise ValueError("Value out of uint32 range")

        return n
x = MergeProtos(folder="defold-sdk")