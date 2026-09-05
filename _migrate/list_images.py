from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)

    
    
    q = [
        {"id": "1Nw8HK-qv5EZWuTj0mvnf5wZtQ7vbWkR_", "path": "understanding-hopfield-network/"},
        {"id": "1E7HQteH7rOmcViXvMFdwam9LG_s-ckmd", "path": "english-learning-journey/"},
        {"id": "1aCnBgXZj0Ewisyt3V1QapUQilGyYJkfQ", "path": "cat-vocabulary/"},
        {"id": "1S9WAIvTSghA8_RWmu8-mn68J3I_W1iVQ", "path": "understanding-transformer-part-2/"},
        {"id": "1OtCsO040p7F_HbnwglEBQOxfX1FOvo9d", "path": "trigonometric-identities-with-geometry/"},
        {"id": "1bO8i1B3nE-WfDq4pHTP5SwIy0wXJOKZP", "path": "understanding-bert/"},
        {"id": "1DzlVy186Hi5724g8HJP9DF-4lij9f1Ji", "path": "biology-of-a-large-language-model/"},
        {"id": "1eYze24XEQNHiPCgdvFAKNFG1e0YkSHsu", "path": "understanding-information-entropy/"},
        {"id": "1eV20w1erX_2YxRHcGb3VPoA33qD2fhS0", "path": "understanding-optimizer/"},
        {"id": "1cK_Xv4rYxZcl2UYinDRjba-YSYo4aQat", "path": "understanding-transformer-part-3/"},
        {"id": "1zVq_vUtUI7YcYeHvHOXkx-q70PHmKHG0", "path": "hulks-cat/"},
        {"id": "1eqVFiOF-RFhLKVdUJPrMvTh85tk-t6PU", "path": "understanding-shap/"},
        {"id": "1JPvOWt0mlNjUwbC8JGxBRiVpKUeoUvCy", "path": "understanding-transformer-part-1/"},
    ]
    # with open("img_folders.csv") as fin:
    #     for line in fin:
    #         line = line.strip().split(",")
    #         q.append({
    #             "id": line[1],
    #             "path": line[0]
    #         })

 
    fin = open("_imgs.csv", "w")
    while len(q)>0:
        target_folder = q.pop()
        target_folder_path = target_folder["path"]
        target_folder_id = target_folder["id"]
        print("ls", target_folder_path)

        page_token = None
        while True:
            response = service.files().list(q=f"('{target_folder_id}' in parents) and (mimeType contains 'image/' or mimeType contains 'video/')",
                                                spaces='drive',
                                                fields='nextPageToken, files(id, name)',
                                                pageToken=page_token).execute()
            for file in response.get('files', []):
                # Process change
                o = {
                    "id": file.get('id'),
                    "path": target_folder_path+file.get('name')
                }

                fin.write(f"{o['path']},{o['id']}\n")
            page_token = response.get('nextPageToken', None)
            if page_token is None:
                break

    fin.close()

if __name__ == '__main__':
    main()