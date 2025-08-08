import os


for filename in os.listdir("../ProPresenter7-Proto/proto/"):
    if filename.endswith(".proto"):
        protoc_command = 'protoc {} --proto_path="../ProPresenter7-Proto/proto" --python_out="src/"'.format(filename)
        os.system(protoc_command) 
        protoc_pyi_command = 'protoc {} --proto_path="../ProPresenter7-Proto/proto" --pyi_out="src/"'.format(filename)
        os.system(protoc_pyi_command) 