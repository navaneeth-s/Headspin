
import json
import os
from lib.headspin_api import HSAPI

def custom_data_to_description(custom_data):
    description_string = ""
    for key in custom_data:
        description_string += key + " : " + str(custom_data[key]) + "\n"
    return description_string

def description_to_object(description):
    description_list = description.split('\n')
    custom_data = {}
    for description_line in description_list:
        description_line_split = description_line.split(':')
        if len(description_line_split) >= 2:
            key = description_line_split[0].strip()
            value = description_line_split[1]
        else:
            key = description_line_split[0].strip()
            value = 'N/A'
        if key:
            custom_data[key] = value
    return custom_data

class manualSessionLabel:
    def __init__(self, access_token):
        self.access_token = access_token
        self.hs_api = HSAPI(self.access_token)
    def sync_data(self, session_id, user_flow_id):
        '''
            1. Check Google Play DB for source of truth
            2. Check GCP DB for source of truth
            3. Update GCP DB with new data
            4. Update Google Play DB for new data
        '''
        print(session_id)
        print(user_flow_id)
        labels = self.get_labels(session_id)
        description = self.hs_api.get_description(session_id)
        #print(json.dumps(labels, indent=2))
        
        label_custom_data = {}
        #print (labels)
        for label in labels['labels']:
            if label['category'] and 'kpi' in label['category']:
                value = label['end_time'] - label['start_time']
                #print(label['name'], value)
                label_custom_data[label['name']] = value
        print(description['name'])
        print(description['description'])
        print('----------------')
        description_custom_data = description_to_object(description['description'])
        print(description_custom_data)

        for key in label_custom_data:
            if key in description_custom_data:
                description_custom_data[key] = label_custom_data[key]
        # Adding trail that it was updated
        label_custom_data['manual_update'] = True
        description_custom_data['manual_update'] = True
        new_description = custom_data_to_description(description_custom_data)
        print('new_description')
        print(new_description)
        print('label_custom_data')
        print(label_custom_data)
        self.hs_api.attach_session_to_user_flow(session_id, custom_data=label_custom_data)
        self.hs_api.update_session_name_and_description(session_id, description['name'], new_description)
    def get_labels(self, session_id):
        labels = self.hs_api.get_labels(session_id)
        return labels

def main(args):
    sync_manual_session_label_data_flag = args.sync_manual_session_label_data
    session_id = args.session_id
    access_token = args.access_token
    user_flow_id = args.user_flow_id
    if sync_manual_session_label_data_flag and session_id and access_token and user_flow_id:
        msl = manualSessionLabel(access_token)
        msl.sync_data(session_id, user_flow_id)
    else:

        parser.print_help()
        example_cmd_list = ['python', os.path.basename(__file__), '--sync_manual_session_label_data', '--access_token', '<access_token>']
        example_cmd_list += ['--user_flow_id', '<user_flow_id>', '--session_id', '<session_id>']
        print(' '.join(example_cmd_list))
        
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    # flags
    parser.add_argument('--sync_manual_session_label_data', '--sync_manual_session_label_data',
                        dest='sync_manual_session_label_data',
                        action='store_true',
                        default=None,
                        required=False,
                        help="sync_manual_session_label_data")

    # Args
    parser.add_argument('--session_id', '--session_id', dest='session_id',
                        type=str, nargs='?',
                        default=None,
                        required=False,
                        help="session_id")
    parser.add_argument('--access_token', '--access_token', dest='access_token',
                        type=str, nargs='?',
                        default=None,
                        required=False,
                        help="access_token")
    parser.add_argument('--user_flow_id', '--user_flow_id', dest='user_flow_id',
                        type=str, nargs='?',
                        default=None,
                        required=False,
                        help="user_flow_id")
                        
    args = parser.parse_args()
    main(args)
