/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package br.ifce.so.projeto;

import javax.swing.JLabel;

/**
 *
 * @author Nonato Dias
 */
public class Caixa {
    private String nome;
    private int time;
    private final JLabel jlabel;
    private int posicao_X;
    private boolean caixaOcupado;

    public boolean isCaixaOcupado() {
        return caixaOcupado;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    
    public int getTime() {
        return time;
    }

    public void setTime(int time) {
        this.time = time;
    }

    
    public void setCaixaOcupado(boolean caixaOcupado) {
        this.caixaOcupado = caixaOcupado;
    }
    
    public int getPosicao_X() {
        return posicao_X;
    }

    public void setPosicao_X(int posicao_X) {
        this.posicao_X = posicao_X;
    }

    
    public Caixa(String nome, int time, JLabel jlabel, int posicao_X) {
        this.nome = nome;
        this.time = time;
        this.jlabel = jlabel;
        this.jlabel.setVisible(false);
        this.posicao_X = posicao_X;
        caixaOcupado = false;
        
    }

     public void movimentaDinheiro(int tempo){
         int a = 1;
        jlabel.setVisible(true);
        for(int h=0; h<tempo; h++){
            jlabel.setIcon(new javax.swing.ImageIcon(getClass().getResource("/br/ifce/so/projeto/display/imagens/caixaFeliz.png")));
            for(int i = 0; i<100000; i++)
                for(int j= 0; j<10000;j++)
                    a = 2*a;
            jlabel.setIcon(new javax.swing.ImageIcon(getClass().getResource("/br/ifce/so/projeto/display/imagens/caixaVazio.png")));
            for(int i = 0; i<100000; i++)
                for(int j= 0; j<10000;j++)
                    a = 2*a;
        }
        jlabel.setVisible(false);
    }
}
