import {Client} from '@notionhq/client';

const notion = new Client({
    auth: process.env.API_KEY
});

export default async function main(){

    await notion.pages.create({
        
    })
    
}
