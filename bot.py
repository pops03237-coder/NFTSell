import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# 🔐 Ваш API-ключ бота
TOKEN = "8550146768:AAHfgRi2WhEHeUBvXC-nJMlHLMqB47GheEc"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /start с инлайн-клавиатурой"""
    try:
        keyboard = [
            [InlineKeyboardButton("🎁 NFT Подарки", callback_data="nft_gifts")],
            [InlineKeyboardButton("⭐ Telegram Stars", callback_data="stars")],
            [InlineKeyboardButton("👑 Telegram Premium", callback_data="premium")],
            [InlineKeyboardButton("💎 TON Coin", callback_data="ton")],
            [InlineKeyboardButton("📞 Поддержка", callback_data="support")],
            [InlineKeyboardButton("ℹ️ О нас", callback_data="about")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        welcome_text = (
            "🎄 **Добро пожаловать в NFT Gifts Shop!** 🎄\n\n"
            "✨ *Создаем уникальные цифровые подарки:*\n"
            "• Персонализированные NFT 🎨\n"
            "• Подарочные сертификаты 🎁\n"
            "• Цифровые открытки 💌\n"
            "• Коллекционные предметы 🏆\n\n"
            "👇 *Выберите категорию:*"
        )
        
        if update.message:
            await update.message.reply_text(welcome_text, reply_markup=reply_markup, parse_mode='Markdown')
        else:
            await update.callback_query.message.reply_text(welcome_text, reply_markup=reply_markup, parse_mode='Markdown')
            
    except Exception as e:
        logger.error(f"Ошибка в start: {e}")

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик нажатий на кнопки"""
    query = update.callback_query
    await query.answer()
    
    try:
        if query.data == "nft_gifts":
            keyboard = [
                [InlineKeyboardButton("🎨 Персонализированные NFT", callback_data="personal_nft")],
                [InlineKeyboardButton("💌 Цифровые открытки", callback_data="digital_cards")],
                [InlineKeyboardButton("🏆 Коллекционные предметы", callback_data="collectibles")],
                [InlineKeyboardButton("🎁 Подарочные сертификаты", callback_data="gift_cards")],
                [InlineKeyboardButton("🔙 Назад", callback_data="back_main")]
            ]
            text = (
                "🎁 **NFT Подарки**\n\n"
                "💫 *Выберите тип подарка:*\n"
                "• 🎨 Персонализированные NFT\n"
                "• 💌 Цифровые открытки\n"
                "• 🏆 Коллекционные предметы\n"
                "• 🎁 Подарочные сертификаты\n\n"
                "⚡ Быстрая доставка • 🔒 Гарантия подлинности"
            )
            
        elif query.data == "personal_nft":
            keyboard = [
                [InlineKeyboardButton("💝 Для него", callback_data="for_him")],
                [InlineKeyboardButton("💝 Для нее", callback_data="for_her")],
                [InlineKeyboardButton("🎂 День рождения", callback_data="birthday")],
                [InlineKeyboardButton("💍 Свадьба", callback_data="wedding")],
                [InlineKeyboardButton("🔙 Назад", callback_data="nft_gifts")]
            ]
            text = (
                "🎨 **Персонализированные NFT**\n\n"
                "✨ *Создаем уникальные NFT с персональным дизайном:*\n"
                "• Имя получателя 📝\n"
                "• Персональное послание 💌\n"
                "• Выбор дизайна 🎨\n"
                "• Дата и событие 📅\n\n"
                "💰 *Цены:* от 1000 руб\n"
                "⏱ *Срок:* 1-2 дня\n\n"
                "👇 Выберите повод:"
            )
            
        elif query.data == "digital_cards":
            keyboard = [
                [InlineKeyboardButton("🎄 Новый год", callback_data="new_year")],
                [InlineKeyboardButton("💘 День святого Валентина", callback_data="valentine")],
                [InlineKeyboardButton("🎂 День рождения", callback_data="bday_card")],
                [InlineKeyboardButton("🎓 Выпускной", callback_data="graduation")],
                [InlineKeyboardButton("🔙 Назад", callback_data="nft_gifts")]
            ]
            text = (
                "💌 **Цифровые открытки NFT**\n\n"
                "🎴 *Коллекционные цифровые открытки:*\n"
                "• Анимированные дизайны ✨\n"
                "• Ограниченный тираж 🏷️\n"
                "• Персональное сообщение 📝\n"
                "• Высокое качество 🖼️\n\n"
                "💰 *Цены:* 500-2000 руб\n"
                "⚡ *Доставка:* мгновенно"
            )
            
        elif query.data == "stars":
            keyboard = [
                [InlineKeyboardButton("⭐ 100 Stars - 500 руб", callback_data="stars_100")],
                [InlineKeyboardButton("⭐⭐ 500 Stars - 2000 руб", callback_data="stars_500")],
                [InlineKeyboardButton("⭐⭐⭐ 1000 Stars - 3500 руб", callback_data="stars_1000")],
                [InlineKeyboardButton("🔙 Назад", callback_data="back_main")]
            ]
            text = (
                "⭐ **Telegram Stars**\n\n"
                "💫 *Внутренняя валюта Telegram:*\n"
                "• Покупка цифровых товаров 🛍️\n"
                "• Поддержка создателей 💝\n"
                "• Быстрые транзакции ⚡\n\n"
                "👇 Выберите пакет:"
            )
            
        elif query.data == "premium":
            keyboard = [
                [InlineKeyboardButton("👑 1 месяц - 500 руб", callback_data="premium_1")],
                [InlineKeyboardButton("👑👑 3 месяца - 1200 руб", callback_data="premium_3")],
                [InlineKeyboardButton("👑👑👑 12 месяцев - 3500 руб", callback_data="premium_12")],
                [InlineKeyboardButton("🔙 Назад", callback_data="back_main")]
            ]
            text = (
                "👑 **Telegram Premium**\n\n"
                "🌟 *Премиум возможности:*\n"
                "• Увеличенные лимиты 📊\n"
                "• Эксклюзивные стикers ✨\n"
                "• Быстрые загрузки ⚡\n"
                "• Премиум значек 💎\n\n"
                "👇 Выберите период:"
            )
            
        elif query.data == "ton":
            keyboard = [
                [InlineKeyboardButton("💎 100 TON - 10000 руб", callback_data="ton_100")],
                [InlineKeyboardButton("💎💎 500 TON - 45000 руб", callback_data="ton_500")],
                [InlineKeyboardButton("💎💎💎 1000 TON - 85000 руб", callback_data="ton_1000")],
                [InlineKeyboardButton("🔙 Назад", callback_data="back_main")]
            ]
            text = (
                "💎 **TON Coin**\n\n"
                "🚀 *Криптовалюта Telegram:*\n"
                "• Быстрые транзакции ⚡\n"
                "• Низкие комиссии 💰\n"
                "• Растущий потенциал 📈\n\n"
                "👇 Выберите количество:"
            )
            
        elif query.data == "support":
            keyboard = [
                [InlineKeyboardButton("💬 Написать менеджеру", url="https://t.me/manager_account")],
                [InlineKeyboardButton("🔙 Назад", callback_data="back_main")]
            ]
            text = (
                "📞 **Служба поддержки**\n\n"
                "👨‍💼 *Наши менеджеры:*\n"
                "• @nft_manager - NFT подарки 🎁\n"
                "• @stars_manager - Telegram Stars ⭐\n"
                "• @premium_manager - Premium 👑\n"
                "• @crypto_manager - TON Coin 💎\n\n"
                "⏰ *Работаем 24/7*\n"
                "⚡ *Ответ за 5-15 минут*"
            )
            
        elif query.data == "about":
            keyboard = [
                [InlineKeyboardButton("🔙 Назад", callback_data="back_main")]
            ]
            text = (
                "ℹ️ **О нас**\n\n"
                "🎄 **NFT Gifts Shop** - создаем уникальные цифровые подарки!\n\n"
                "✨ *Наши преимущества:*\n"
                "• Уникальные дизайны 🎨\n"
                "• Быстрая доставка ⚡\n"
                "• Гарантия подлинности 🔒\n"
                "• Поддержка 24/7 📞\n\n"
                "💝 *Дарите эмоции в цифровом формате!*"
            )
            
        elif query.data == "back_main":
            await start(update, context)
            return
            
        else:
            # Для всех остальных кнопок - заказ
            keyboard = [
                [InlineKeyboardButton("💬 Заказать", url="https://t.me/manager_account")],
                [InlineKeyboardButton("🔙 Назад", callback_data="back_main")]
            ]
            text = (
                "🎉 **Отличный выбор!**\n\n"
                "💫 *Для оформления заказа:*\n"
                "1. Нажмите '💬 Заказать'\n"
                "2. Укажите детали заказа\n"
                "3. Получите подтверждение\n\n"
                "⚡ *Доставка:* 1-24 часа\n"
                "🔒 *Гарантия:* 100% безопасность"
            )
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=text, reply_markup=reply_markup, parse_mode='Markdown')
        
    except Exception as e:
        logger.error(f"Ошибка в button_handler: {e}")

def main():
    """Основная функция"""
    try:
        logger.info("Запуск NFT Gifts Shop бота...")
        
        # Создаем приложение
        application = Application.builder().token(TOKEN).build()
        
        # Добавляем обработчики
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CallbackQueryHandler(button_handler))
        
        # Запускаем бота
        logger.info("Бот запускается...")
        application.run_polling()
        logger.info("Бот успешно запущен!")
        
    except Exception as e:
        logger.error(f"Ошибка запуска бота: {e}")

if __name__ == '__main__':
    main()
