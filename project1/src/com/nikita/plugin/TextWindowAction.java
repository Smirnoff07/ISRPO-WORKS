package com.nikita.plugin;

import com.intellij.openapi.actionSystem.AnAction;
import com.intellij.openapi.actionSystem.AnActionEvent;
import com.intellij.openapi.ui.Messages;

public class TextWindowAction  extends AnAction {
    @Override
    public void actionPerformed(AnActionEvent e) {
        Messages.showInfoMessage("Плагин работает!", "Успех");
    }
}


