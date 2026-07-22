from app.database import supabase

try:
    response = (
        supabase
        .table("products")
        .select("*")
        .limit(5)
        .execute()
    )

    print("✅ Connected to Supabase Successfully!")
    print(response.data)

except Exception as e:
    print("❌ Connection Failed")
    print(e)