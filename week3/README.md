# Assignment Week 3 - PokeAPI MCP Server

## Setup
1. Aktifkan venv: `source venv/bin/activate` atau `.\venv\Scripts\Activate.ps1`
2. Jalankan inspector: `npx @modelcontextprotocol/inspector python main.py`

## Tools
1. `get_pokemon_info`: Mengambil info tipe dan berat pokemon.
2. `get_pokemon_ability`: Mengambil deskripsi efek kemampuan pokemon.

## Error Handling
Menggunakan blok `try-except` dengan `httpx` untuk menangkap error 404 jika pokemon/ability tidak ditemukan, serta menangani kendala *timeout* jaringan.