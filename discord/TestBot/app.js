const Discord = require("discord.js");
const client = new Discord.Client();
const token = require('./settings.json').token;

client.on("ready", () => {
    console.log("I'm online !!!");
});

var prefix = "$"

client.on("message", message => {
    if (message.author.bot) return;

    if (!message.content.startsWith(prefix)) return;

    args = message.content.substring(prefix.length).toLowerCase().split(" ")
    switch (args[0]) {
        case "ping":
            message.channel.send("Pong! " + `${Date.now() - message.createdTimestamp}`);
            break;
        case "boss":
            switch (args[1]) {
                case "dead":
                    if (!args[2]):
                    break;
                default:
                    break;
            }
            break;
        default:
            message.channel.send("Command not found :(");
    }
});

client.login(token);