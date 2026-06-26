// api/webhook.js
// Vercel serverless function — Telegram calls this URL directly (a "webhook")
// every time someone sends your bot a message. No polling, no always-on process.

const BOT_TOKEN = process.env.BOT_TOKEN;
const TELEGRAM_API = `https://api.telegram.org/bot${8759870497:AAE3NaY0HohTRukG-mqnQxQUb2zSebEuxyI}`;

const TRANSMISSION = [
  "Hello.",
  "We have been watching.",
  "You have been chosen.",
  "Seven fragments remain, scattered across a story you already know.",
  "01.01.01",
  "02.01.01",
  "03.01.01",
  "04.01.01",
  "05.01.01",
  "06.01.01",
  "07.01.01",
  "Find out what it's about.",
  "When the fragments are recovered, a single word will remain.",
  "What single word connects all recovered clues?",
].join("\n");

async function sendMessage(chatId, text) {
  await fetch(`${TELEGRAM_API}/sendMessage`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ chat_id: chatId, text }),
  });
}

export default async function handler(req, res) {
  // Telegram sends a POST request for every update (message, command, etc.)
  if (req.method !== "POST") {
    res.status(200).send("Cicada webhook is alive.");
    return;
  }

  try {
    const update = req.body;
    const message = update?.message;
    const chatId = message?.chat?.id;
    const text = message?.text || "";

    if (chatId && text.startsWith("/start")) {
      await sendMessage(chatId, TRANSMISSION);
    }

    // Always respond 200 quickly so Telegram doesn't retry/flag the webhook
    res.status(200).json({ ok: true });
  } catch (err) {
    console.error("Webhook error:", err);
    res.status(200).json({ ok: true }); // still 200 — avoid Telegram retry storms
  }
}
