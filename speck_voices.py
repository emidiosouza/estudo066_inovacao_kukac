from elevenlabs import Voice, VoiceSettings, generate, play, set_api_key


set_api_key("3458a35b30be9a8d616d3cd8da97f26f")

audio = generate(
    text="Meu nome é Léo, e sou a voz da Kukac no Speck EAD.",
    model="eleven_multilingual_v2",
    voice=Voice(
        voice_id='5dc0VM8bcbHwfxQocbuA',
        settings=VoiceSettings(stability=0.5, similarity_boost=1, style=0.0, use_speaker_boost=True)
    )
)

play(audio)