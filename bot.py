import os
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

TOKEN = os.getenv("7576124345:AAHtXI97MUrufKaZUfIsH7eFjNRsXQkMHEI")
FILE_PATH = "yourfile.txt"  # Change this to your actual file

bot = Bot(token=TOKEN)

async def start(update: Update, context: CallbackContext):
    """Handles /start command with optional parameters."""
    args = context.args  # Get arguments after /start

    if args:
        param = args[0]  # Extract parameter from /start
        await update.message.reply_text(f"Received parameter: {param}")

        # Send file
        with open(FILE_PATH, "rb") as file:
            await update.message.reply_document(file, caption="Here is your file.")

        # Delete file after sending
        os.remove(FILE_PATH)
        print(f"{FILE_PATH} deleted.")
    else:
        await update.message.reply_text("Welcome! Click a special link to get your file.")

# Main function to run bot
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
