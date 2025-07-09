from pyflowchart import Flowchart


def generate_dot_file(code_path, output_dot="flowchart.dot"):
    """
    将Python代码转换为Graphviz .dot文件
    :param code_path: 输入Python文件路径
    :param output_dot: 输出.dot文件路径
    """
    # 读取代码
    with open(code_path, "r", encoding="utf-8") as f:
        code = f.read()

    # 生成流程图DSL（flowchart.js格式）
    fc = Flowchart.from_code(code, simplify=True)
    dsl = fc.flowchart()

    # 转换DSL为Graphviz兼容格式
    # 注：pyflowchart原生支持-f dot参数，此处为手动适配示例
    dot_code = f"digraph G {{\n    node [shape=box, style=filled, color=lightblue];\n    {dsl.replace('=>', '->').replace('[', '{').replace(']', '}')}\n}}"

    # 保存为.dot文件
    with open(output_dot, "w", encoding="utf-8") as f:
        f.write(dot_code)
    print(f"✅ .dot文件生成成功：{output_dot}")


if __name__ == "__main__":
    generate_dot_file("example.py")  # 输入你的Python代码文件