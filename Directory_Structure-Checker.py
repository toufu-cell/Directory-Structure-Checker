import os

def generate_md_tree(dir_path, indent_level=0, is_last=True):
    """
    指定したディレクトリ配下のファイル・ディレクトリ構造を
    Markdownのリスト記法で再帰的に文字列として返す。
    """
    # 返却用の文字列バッファ
    md_tree_str = ""

    # ディレクトリ名をMarkdownのリスト形式で追加
    if indent_level == 0:
        # ルートディレクトリの場合
        md_tree_str += f"- **{os.path.basename(dir_path)}**\n"
    else:
        md_tree_str += "  " * indent_level + f"- **{os.path.basename(dir_path)}/**\n"

    # ディレクトリに含まれる要素を取得
    entries = sorted(os.listdir(dir_path))

    # 最後の要素かどうかを判断するためにループ時に使うカウンタ
    total_entries = len(entries)
    count = 0

    # ディレクトリ配下の各エントリ（ファイルまたはサブディレクトリ）を処理
    for entry in entries:
        count += 1
        full_path = os.path.join(dir_path, entry)

        # サブディレクトリの場合、再帰的に構造を取得
        if os.path.isdir(full_path):
            # ディレクトリを再帰的に追加
            md_tree_str += generate_md_tree(
                full_path,
                indent_level=indent_level + 1,
                is_last=(count == total_entries)
            )
        else:
            # ファイルの場合、単純にリストアイテムとして追加
            md_tree_str += "  " * (indent_level + 1) + f"- {entry}\n"

    return md_tree_str


if __name__ == "__main__":
    # ユーザーにフォルダのパスの入力を求める
    target_directory = input("ツリー構造を生成したいフォルダのパスを入力してください: ").strip()
    
    # パスの正規化（余分な区切り文字の削除やパスの標準化）
    target_directory = os.path.normpath(target_directory)

    # パスが存在するか確認
    if not os.path.exists(target_directory):
        print(f"指定されたパス '{target_directory}' が存在しません。")
        exit(1)

    if not os.path.isdir(target_directory):
        print(f"指定されたパス '{target_directory}' はディレクトリではありません。")
        exit(1)

    # ファイル構造をMarkdown形式で取得
    md_tree = generate_md_tree(target_directory)

    # 表示
    print("\n生成されたディレクトリ構造：\n")
    print(md_tree)
