import sys


def launch_tool():
    root = r"C:\Users\malo.muylaert\Desktop\exo\renamer"
    if root not in sys.path:
        sys.path.append(root)

    import ui.main_ui as main_ui
    main_ui.show_renamer()

if __name__ == "__main__":
    launch_tool()
