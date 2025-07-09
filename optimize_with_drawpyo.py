import drawpyo
from drawpyo.diagram_types import TreeDiagram, NodeObject


def create_tree_diagram(output_path="optimized.drawio"):
    """使用Drawpyo创建自动布局的树形流程图"""
    # 初始化TreeDiagram（自动布局）
    tree = TreeDiagram(
        file_name=output_path,
        direction="down",  # 布局方向：down/up/left/right
        level_spacing=80,  # 层级间距
        item_spacing=20  # 节点间距
    )

    # 创建节点（树形结构）
    root = NodeObject(tree=tree, value="开始")
    node1 = NodeObject(tree=tree, value="处理步骤1", tree_parent=root)
    node2 = NodeObject(tree=tree, value="判断条件", tree_parent=node1)
    node3 = NodeObject(tree=tree, value="处理步骤2", tree_parent=node2)
    node4 = NodeObject(tree=tree, value="结束", tree_parent=node3)

    # 保存文件
    tree.write()
    print(f"✅ 优化后的draw.io文件：{output_path}")


if __name__ == "__main__":
    create_tree_diagram()