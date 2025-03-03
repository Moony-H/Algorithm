import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: process.env.OPENAI_API_KEY
});

const messages = [
    { role: "system", content: "You're a consumer-friendly print solution assistant using big data." },
    {
        role: "user",
        content: `
        A solution that reduces consumer price trial and error (time, cost, quality)
        during the printing process and improves the work efficiency of printing companies
        by proposing customized printing specifications for consumers through AI.
        Here is the question: ...
        `
    }
    //생략...
];

const completion = await openai.chat.completions.create({
    model: "gpt-4o",
    messages,
    temperature: 0.7
});

console.log(completion.choices[0].message.content);