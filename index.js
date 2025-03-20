const login = require("fca-unofficial");
const fs = require("fs");

// Facebook लॉगिन डिटेल्स
const credentials = {
    email: "61573484631602",
    password: "allahkutta@786"
};

// टारगेट ग्रुप ID की लिस्ट
const groupIDs = [
    "7032090300237636",
    "GROUP_ID_2",
    "GROUP_ID_3",
    // और ग्रुप IDs ऐड करें
];

// ऑटो-जनरेटेड निकनेम की लिस्ट
const nicknames = ["King", "Boss", "Legend", "Pro Player", "Champion", "Master", "Warrior", "Hero"];

// लॉगिन करें और बॉट स्टार्ट करें
login(credentials, (err, api) => {
    if (err) return console.error("Login Failed:", err);
    console.log("Bot is now online and running...");
    
    async function updateNicknames() {
        for (const groupID of groupIDs) {
            api.getThreadInfo(groupID, (err, info) => {
                if (err) return console.error("Failed to get group info for:", groupID);
                
                info.participantIDs.forEach((userID) => {
                    let randomNickname = nicknames[Math.floor(Math.random() * nicknames.length)];
                    api.changeNickname(randomNickname, groupID, userID, (err) => {
                        if (err) console.error(`Failed to change nickname for ${userID} in group ${groupID}`);
                        else console.log(`Nickname changed to '${randomNickname}' for user ${userID} in group ${groupID}`);
                    });
                });
            });
        }
    }
    
    // हर 5 मिनट में ऑटोमैटिकली निकनेम बदलें
    setInterval(updateNicknames, 5 * 60 * 1000);
    updateNicknames();
});
