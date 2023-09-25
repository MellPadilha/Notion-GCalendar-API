import {Client} from '@notionhq/client';

const notion = new Client({
    auth: process.env.API_KEY
});

export default async function main(){

    
    function insertEvent(EventsList){
        EventsList.forEach(event => {
            notion.pages.create({
                "parent": {
                    "type": "database_id",
                    "database_id": process.env.KEY_PAGE
                },
                "properties": {
                    "Name": {
                        "title": [
                            {
                                "text": {
                                    "content": event.name
                                }
                            }
                        ]
                    },
                    "Start": {
                        "date": {
                              "start": event.startDate
                            }
                    },
                    "End": {
                        "date": {
                              "start": event.endDate
                            }
                    }
                }
        })
        console.log(response);

        });
    }
    async function EditEvent(EventId, changedFields){
        const pageId = '59833787-2cf9-4fdf-8782-e53db20768a5';
        const response = await notion.pages.retrieve({ page_id: pageId });
        console.log(response);
    };

    
}
