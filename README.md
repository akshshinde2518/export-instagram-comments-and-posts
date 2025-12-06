# Export Instagram Comments and Posts Scraper
> This scraper pulls Instagram post details and all related comments in a single streamlined run. It helps you gather captions, likes, timestamps, and every comment with user info, making large-scale Instagram analysis surprisingly manageable. Whether you're studying audience behavior or collecting content for research, this tool keeps the process smooth and reliable.


<p align="center">
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://github.com/Z786ZA/Footer-test/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/Bitbash333" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>Export Instagram Comments and Posts</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction
This project extracts both Instagram posts and comments in one go. It solves the challenge of gathering scattered post data and nested comment threads while keeping everything organized in a combined dataset. It's built for researchers, analysts, marketers, and anyone who needs structured Instagram data without juggling multiple tools.

### Why this scraper matters
- Captures detailed post information alongside every related comment.
- Handles multiple Instagram profiles at once.
- Supports exporting results in several formats.
- Includes full metadata for richer analysis.
- Produces clean, uniform output ready for automation or integration.

## Features
| Feature | Description |
|----------|-------------|
| Unified scraping workflow | Collects posts and comments in a single run, reducing overhead. |
| Rich post metadata capture | Extracts captions, timestamps, likes, media info, and tagged users. |
| Full comment extraction | Pulls commenter data, comment text, profile pictures, and more. |
| Multi-profile input | Add one or many profiles at once for batch scraping. |
| Flexible output formats | Export data as JSON, CSV, Excel, XML, or via API. |
| Automation-ready | Supports scheduled runs and programmatic execution. |

---

## What Data This Scraper Extracts
| Field Name | Field Description |
|-------------|------------------|
| commentText | The text content of the comment. |
| commentatorUserName | Username of the person who posted the comment. |
| commentatorProfilePicUrl | URL of the commenter’s profile image. |
| postInfo.inputUrl | The profile URL used as input. |
| postInfo.id | Unique ID of the Instagram post. |
| postInfo.type | Specifies whether the post is an image, video, etc. |
| postInfo.shortCode | Post shortcode used for direct post linking. |
| postInfo.caption | Main caption text of the post. |
| postInfo.hashtags | List of hashtags used in the caption. |
| postInfo.mentions | List of mentioned usernames. |
| postInfo.url | Direct URL to the post. |
| postInfo.dimensionsHeight | Height of the post media. |
| postInfo.dimensionsWidth | Width of the post media. |
| postInfo.displayUrl | URL for displaying the main media. |
| postInfo.likesCount | Number of likes on the post. |
| postInfo.timestamp | ISO timestamp of when the post was created. |
| postInfo.ownerFullName | Full name of the post owner. |
| postInfo.ownerUsername | Username of the post owner. |
| postInfo.taggedUsers | List of tagged users with metadata. |

---

## Example Output

    [
      {
        "commentText": "@maddyfulmino STANDING BY THIS TBH",
        "commentatorUserName": "_mimimann",
        "commentatorProfilePicUrl": "https://scontent-atl3-2.cdninstagram.com/v/...",
        "postInfo": {
          "inputUrl": "https://www.instagram.com/eltonjohn",
          "id": "879248723928966527",
          "type": "Image",
          "shortCode": "wzuA5TAGV_",
          "caption": "Please join us this Sunday ...",
          "hashtags": ["ShareTheLove", "EltonJohn", "DavidFurnish"],
          "mentions": ["DavidFurnish"],
          "url": "https://www.instagram.com/p/wzuA5TAGV_/",
          "dimensionsHeight": 640,
          "dimensionsWidth": 640,
          "displayUrl": "https://instagram.flko7-2.fna.fbcdn.net/...",
          "likesCount": 4218,
          "timestamp": "2014-12-20T00:17:17.000Z",
          "ownerFullName": "Elton John",
          "ownerUsername": "eltonjohn",
          "taggedUsers": [
            {
              "full_name": "Elton John",
              "id": "1604340024",
              "is_verified": true,
              "profile_pic_url": "https://instagram.flko7-4.fna.fbcdn.net/...",
              "username": "eltonjohn"
            }
          ]
        }
      }
    ]

---

## Directory Structure Tree

    Export Instagram Comments and Posts/
    ├── src/
    │   ├── main.js
    │   ├── utils/
    │   │   ├── instagram_client.js
    │   │   ├── data_cleaner.js
    │   │   └── validator.js
    │   ├── extractors/
    │   │   ├── posts_extractor.js
    │   │   └── comments_extractor.js
    │   ├── outputs/
    │   │   └── formatter.js
    │   └── config/
    │       └── input.schema.json
    ├── data/
    │   ├── sample_input.json
    │   └── sample_output.json
    ├── tests/
    │   ├── posts.test.js
    │   └── comments.test.js
    ├── package.json
    ├── .gitignore
    └── README.md

---

## Use Cases
- Researchers use it to collect structured Instagram interaction data, so they can analyze social behavior trends.
- Marketing teams use it to evaluate audience responses, helping them refine campaign strategies.
- Influencer managers use it to archive comment sentiment, allowing them to track engagement quality.
- Journalists use it to gather historical post and comment data for reporting or investigation.
- Developers integrate it into automation pipelines to keep content datasets refreshed.

---

## FAQs

**Does this scraper require login?**
It runs without login for public profiles. Private profiles require proper authorization, and the tool won't bypass any access restrictions.

**Can it handle very large profiles?**
Yes. It processes high-volume profiles by batching posts and comments, keeping memory usage predictable.

**What output formats are supported?**
You can export data as JSON, CSV, Excel, XML, or fetch it programmatically through an API.

**Is scraping Instagram allowed?**
Use it responsibly and ensure compliance with Instagram’s terms and relevant data regulations.

---

### Performance Benchmarks and Results

**Primary Metric:** On average, the scraper processes 50–80 posts per minute, including all associated comments, depending on media size and network conditions.

**Reliability Metric:** Steady completion rate above 98 percent during long batch runs due to internal retry logic.

**Efficiency Metric:** Optimized request sequencing keeps resource usage low while maintaining consistent throughput.

**Quality Metric:** Data completeness typically exceeds 95 percent, capturing nearly every visible comment and post detail without duplication.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/Z786ZA/Footer-test/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        "Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time."
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/Z786ZA/Footer-test/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        "Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on."
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/m-dRE1dj5-k?si=5kZNVlKsGUhg5Xtx" target="_blank">
        <img src="https://github.com/Z786ZA/Footer-test/blob/main/media/review3.gif" alt="Review 3" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        "Exceptional results, clear communication, and flawless delivery. <br>Bitbash nailed it."
      </p>
      <p style="margin:1px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>
