import os

from .create_embeddings import create_embeddings


def read_documents(root_dir="docs/Synergy/CSP/trouble_shooting"):
    result = []
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if (file.endswith(".md") or file.endswith(".mdx")) and file!=("in_progress.md"):
                file_path = os.path.join(subdir, file)
                with open(file_path, "r") as f:
                    content = f.read()
                    result.append(content)
    return result

def upload_to_qdrant(embeddings):
    pass


if __name__ == '__main__':
    documents = read_documents()
    embeddings = create_embeddings(documents=documents)
    upload_to_qdrant(embeddings=embeddings)
