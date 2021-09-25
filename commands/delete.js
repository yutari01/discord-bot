const { SlashCommandBuilder } = require('@discordjs/builders');

function message_delete(message, interaction) {
	message.channel.bulkDelete(100, true)
	interaction.reply(':broom')
}

module.exports = {
	data: new SlashCommandBuilder()
		.setName('delete')
		.setDescription('Remove all Message!')
		.addIntegerOption(option =>
			option.setName('value')
				.setDescription('Amount of message that you wanna delete.')
				.setRequired(true)),

	async execute(message, interaction) {
		await message_delete(message, interaction)
	}
};