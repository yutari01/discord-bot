const { SlashCommandBuilder } = require('@discordjs/builders');
const ROKA_END_DATE = new Date(2023, 1, 1, 0, 0, 0, 0);

function getTime() {
	const CURRENT_DATE = new Date();

	let REMAIN_DATE = ROKA_END_DATE - CURRENT_DATE;
	const diffDays = Math.floor((ROKA_END_DATE.getTime() - CURRENT_DATE.getTime()) / (1000 * 60 * 60 * 24));
	REMAIN_DATE -= diffDays * (1000 * 60 * 60 * 24);
	const diffHours = Math.floor(REMAIN_DATE / (1000 * 60 * 60));
	REMAIN_DATE -= diffHours * (1000 * 60 * 60);
	const diffMin = Math.floor(REMAIN_DATE / (1000 * 60));
	REMAIN_DATE -= diffMin * (1000 * 60);
	const diffSec = Math.floor(REMAIN_DATE / 1000);
	
	return `${diffDays < 10 ? `0${diffDays}` : diffDays}일 ${diffHours < 10 ? `0${diffHours}` : diffHours}시간 ${diffMin < 10 ? `0${diffMin}` : diffMin}분 ${diffSec < 10 ? `0${diffSec}` : diffSec}초 남았습니다. 따흑..`;
	}

module.exports = {
	data: new SlashCommandBuilder()
		.setName('roka')
		.setDescription('Calculate the remaining days of ROKA.'),
	async execute(interaction) {
		await interaction.reply(getTime());
	},
};