import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Configuration - Fixed string termination
BOT_TOKEN = "7606251728:AAFZtdI_0VnbnMDUtxKj_si0QezGmdy_aKI"  # Now properly closed
CHANNEL_USERNAME = "@your_channel"  # Change to your channel
GROUP_USERNAME = "@your_group"  # Change to your group
TWITTER_USERNAME = "your_twitter"  # Change to your Twitter

async def start(update: Update, context: CallbackContext):
    user = update.effective_user
    welcome_message = f"""
    🚀 Welcome {user.first_name} to our Airdrop Bot! 🚀

    To participate in the airdrop, please:
    1. Join our channel: {CHANNEL_USERNAME}
    2. Join our group: {GROUP_USERNAME}
    3. Follow us on Twitter: https://twitter.com/{TWITTER_USERNAME}

    After completing these steps, please send your Solana wallet address.
    """
    
    keyboard = [
        [InlineKeyboardButton("Join Channel", url=f"https://t.me/{CHANNEL_USERNAME[1:]}")],
        [InlineKeyboardButton("Join Group", url=f"https://t.me/{GROUP_USERNAME[1:]}")],
        [InlineKeyboardButton("Follow Twitter", url=f"https://twitter.com/{TWITTER_USERNAME}")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(welcome_message, reply_markup=reply_markup)

async def handle_wallet(update: Update, context: CallbackContext):
    wallet_address = update.message.text.strip()
    
    # Fixed if statement syntax
    if len(wallet_address) >= 32 and len(wallet_address) <= 44:
        success_message = f"""
        🎉 Congratulations! 🎉

        You've successfully participated in our airdrop!
        10 SOL is on its way to your wallet: 
        {wallet_address}

        Thank you for your support!
        """
        await update.message.reply_text(success_message)
    else:
        await update.message.reply_text("⚠️ Please enter a valid Solana wallet address.")

def main():
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_wallet))
    
    # Start the Bot
    application.run_polling()

if __name__ == "__main__":
    main()
