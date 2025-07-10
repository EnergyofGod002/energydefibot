Here's the complete Telegram airdrop bot code with your test token included:
```python
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Configuration with your test token
BOT_TOKEN = "7606251728:AAFZtdI_0VnbnMDUtxKj_si0QezGmdy_aKI"
CHANNEL_USERNAME = "@your_channel"  # Change to your channel
GROUP_USERNAME = "@your_group"     # Change to your group
TWITTER_USERNAME = "your_twitter"  # Change to your Twitter

async def start(update: Update, context: CallbackContext):
    user = update.effective_user
    welcome_message = f"""
    🚀 *Welcome {user.first_name} to Our Airdrop!* 🚀

    *To qualify:*
    ✅ Join our channel: {CHANNEL_USERNAME}
    ✅ Join our group: {GROUP_USERNAME}
    ✅ Follow us on Twitter: twitter.com/{TWITTER_USERNAME}

    *Then send your Solana wallet address below*
    """
    
    keyboard = [
        [InlineKeyboardButton("📢 Join Channel", url=f"https://t.me/{CHANNEL_USERNAME[1:]}")],
        [InlineKeyboardButton("👥 Join Group", url=f"https://t.me/{GROUP_USERNAME[1:]}")],
        [InlineKeyboardButton("🐦 Follow Twitter", url=f"https://twitter.com/{TWITTER_USERNAME}")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(welcome_message, parse_mode="Markdown", reply_markup=reply_markup)

async def handle_wallet(update: Update, context: CallbackContext):
    wallet_address = update.message.text.strip()
    
    # Basic Solana address format check
    if wallet_address.startswith(('SOL', 'Sol', 'sol')) or (len(wallet_address) >= 32 and len(wallet_address) <= 44):
        success_message = f"""
        🎉 *Congratulations!* 🎉

        *10 SOL* has been allocated to:
        `{wallet_address}`

        ⏳ *Distribution will occur after verification*
        Thank you for participating!
        """
        await update.message.reply_text(success_message, parse_mode="Markdown")
    else:
        await update.message.reply_text("⚠️ *Invalid wallet format!* Please send a valid Solana wallet address.", parse_mode="Markdown")

def main():
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_wallet))
    
    # Start the Bot
    print("🤖 Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()
```

Key improvements made:
1. Added Markdown formatting for better message appearance
2. Improved wallet validation (checks for SOL prefix)
3. Enhanced congratulatory message with distribution notice
4. Added emojis for better visual appeal
5. Added console log when bot starts
6. Improved button labels with emojis

To use this bot:
1. Replace the social media placeholders with your actual usernames
2. Run with `python main.py`
3. Interact with your bot using `/start`

Remember to revoke this test token when done by talking to @BotFather on Telegram. For production, you should:
1. Use environment variables
2. Implement proper security measures
3. Consider adding user verification
4. Add rate limiting

Would you like me to add any additional features to this bot?
