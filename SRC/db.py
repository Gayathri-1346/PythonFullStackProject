import os
from supabase import create_client, Client
from dotenv import load_dotenv

#load environment variables
load_dotenv()
url=os.getenv("Supabase_url")
key=os.getenv("Supabase_key")

supabase = create_client(url,key)

#Create Task
def create_task(user_id, username, created_at):
    return supabase.table("users").insert({
        "id": user_id,
        "uname":username,
        "created at":created_at
    }).execute()

def get_all_users():
    return supabase.table("users").select("*").order("id").execute()

def update_task(user_id,created_at):
    return supabase.table("users").update({"Created At":created_at}).eq("id",user_id).execute()

def delete_task(user_id) :
    return supabase.table("tasks").delete().eq("id", user_id).execute()

#Questions table
def create_question(question_id, category, level, prompt, answer, created_at):
    return supabase.table("questions").insert({
        "Question id": question_id,
        "Category": category,
        "Level": level,
        "Prompt": prompt,
        "Answer": answer,
        "Created_At": created_at
    }).execute()

# Fetch all questions
def get_questions_by_level(category, level):
    """Fetch all questions of a category & level"""
    return supabase.table("questions").select("*").eq("category", category).eq("level", level).execute()

# Update a question
def update_question(q_id, new_prompt, new_answer):
    """Update question text and answer"""
    return supabase.table("questions").update({
        "prompt": new_prompt,
        "answer": new_answer
    }).eq("id", q_id).execute()

# Delete a question
def delete_question(q_id):
    """Delete a question"""
    return supabase.table("questions").delete().eq("id", q_id).execute()

#Start a game session
def create_session(user_id, level, score, status):
    return supabase.table("game_sessions").insert({
        "user_id": user_id,
        "level": level,
        "score": score,
        "status": status
    }).execute()

#Get all sessions of a user
def get_sessions_by_user(user_id):
    return supabase.table("game_sessions").select("*").eq("user_id", user_id).execute()

#Update session status (in-progress, completed, failed)
def update_session_status(session_id, new_status):
    return supabase.table("game_sessions").update({
        "status": new_status
    }).eq("id", session_id).execute()

#Update session score
def update_session_score(session_id, new_score):
    return supabase.table("game_sessions").update({
        "score": new_score
    }).eq("id", session_id).execute()

#Delete a session
def delete_session(session_id):
    return supabase.table("game_sessions").delete().eq("id", session_id).execute()

if __name__()== "__main__":
    print(get_all_users())
    