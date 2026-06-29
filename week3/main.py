import httpx
from mcp.server.fastmcp import FastMCP

# Inisialisasi FastMCP server
mcp = FastMCP("PokeAPI_MCP")
BASE_URL = "https://pokeapi.co/api/v2"

@mcp.tool()
async def get_pokemon_info(name: str) -> str:
    """Mendapatkan informasi dasar Pokemon (tipe dan berat) berdasarkan nama."""
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{BASE_URL}/pokemon/{name.lower()}", timeout=5.0)
            response.raise_for_status()
            data = response.json()
            
            types = [t["type"]["name"] for t in data["types"]]
            weight = data["weight"]
            
            return f"Pokemon {name.capitalize()} memiliki tipe: {', '.join(types)} dan berat {weight} hectograms."
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                return f"Error: Pokemon '{name}' tidak ditemukan."
            return f"API Error: {e.response.status_code}"
        except httpx.RequestError as e:
            return f"Network/Timeout Error: Gagal menghubungi PokeAPI ({str(e)})."

@mcp.tool()
async def get_pokemon_ability(ability_name: str) -> str:
    """Mendapatkan deskripsi efek dari sebuah ability Pokemon (misal: 'overgrow', 'blaze')."""
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{BASE_URL}/ability/{ability_name.lower()}", timeout=5.0)
            response.raise_for_status()
            data = response.json()
            
            effect = next((entry["effect"] for entry in data["effect_entries"] if entry["language"]["name"] == "en"), "Deskripsi tidak ditemukan.")
            
            return f"Ability '{ability_name.capitalize()}': {effect}"
        except httpx.HTTPStatusError as e:
             if e.response.status_code == 404:
                return f"Error: Ability '{ability_name}' tidak ditemukan."
             return f"API Error: {e.response.status_code}"
        except httpx.RequestError as e:
            return f"Network/Timeout Error: Gagal menghubungi PokeAPI ({str(e)})."

if __name__ == "__main__":
    mcp.run()