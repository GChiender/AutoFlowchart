from graphviz2drawio import graphviz2drawio


def convert_dot_to_drawio(dot_path, output_drawio="output.drawio"):
    """
    将Graphviz .dot文件转换为draw.io兼容XML
    :param dot_path: .dot文件路径
    :param output_drawio: 输出.drawio文件路径
    """
    # 读取.dot文件内容
    with open(dot_path, "r", encoding="utf-8") as f:
        dot_content = f.read()

    # 转换为draw.io XML
    xml_content = graphviz2drawio.convert(dot_content)

    # 保存为.drawio文件
    with open(output_drawio, "w", encoding="utf-8") as f:
        f.write(xml_content)
    print(f"✅ draw.io文件生成成功：{output_drawio}")


if __name__ == "__main__":
    convert_dot_to_drawio("flowchart.dot")  # 输入上一步生成的.dot文件