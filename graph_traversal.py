import tkinter as tk
import time

def dfs(self, current, target_value, code_display,root, step_by_step,visited=None):
    t = int(1/self.speed)*250
    if visited is None:
        visited = set()
    if current in visited or not self.running:
        return
    code_display.highlight_line(2)
    root.after(t)
    visited.add(current)
    code_display.highlight_line(3)
    root.after(t)
    self.update_graph_plot(current, target_value)
    time.sleep(1 / self.speed)
    if self.graph.nodes[current]['value'] == target_value:
        self.update_graph_plot(current, target_value, found=True)
        return
    # if step_by_step:
    #     self.step_event.clear()
    #     self.step_event.wait()
    code_display.highlight_line(4)
    for neighbor in self.graph.neighbors(current):
        if step_by_step:
            self.step_event.clear()
            self.step_event.wait()
        code_display.highlight_line(4)
        root.after(t)
        dfs(self,neighbor, target_value,code_display,root,step_by_step ,visited)
        code_display.highlight_line(5)
        root.after(t)
    if current == 0 and not self.running:
        self.update_graph_plot(found=False)

def bfs(self, start_node, target_value, code_display, root,step_by_step):
    t = int(1/self.speed)*250
    queue = [start_node]
    code_display.highlight_line(2)
    root.after(t)
    visited = set()
    code_display.highlight_line(3)
    root.after(t)
    code_display.highlight_line(4)
    while queue and self.running:
        # if step_by_step:
        #     self.step_event.clear()
        #     self.step_event.wait()
        code_display.highlight_line(4)
        root.after(t)
        code_display.highlight_line(5)
        root.after(t)
        current = queue.pop(0)
        if current in visited:
            continue
        code_display.highlight_line(6)
        root.after(t)
        visited.add(current)

        self.update_graph_plot(current, target_value)
        time.sleep(1 / self.speed)
        if self.graph.nodes[current]['value'] == target_value:
            self.update_graph_plot(current, target_value, found=True)
            return
        code_display.highlight_line(7)
        root.after(t)
        queue.extend(neighbor for neighbor in self.graph.neighbors(current) if neighbor not in visited)
        if step_by_step:
            self.step_event.clear()
            self.step_event.wait()
    self.update_graph_plot(found=False)

