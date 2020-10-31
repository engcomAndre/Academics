/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package br.ifce.so.projeto;

import static java.lang.Thread.sleep;
import javax.swing.JLabel;

/**
 *
 * @author Nonato Dias
 */
public class Cliente {
    
    private Caixa caixa;
    private int senha;
    private JLabel jlabel;
    private boolean emUso;
    private int tempo;
    private int imagemCliente;

    public Cliente(JLabel jlabel, int tempo, int senha, Caixa caixa) {
        this.jlabel = jlabel;
        this.senha = senha;
        this.tempo = tempo;
        this.imagemCliente = 1;
        this.emUso = true;
        this.caixa = caixa;
    }
    
    public void setEmUso(boolean emUso) {
        this.emUso = emUso;
    }

    public int getSenha() {
        return senha;
    }

    public void setSenha(int senha) {
        this.senha = senha;
    }

    public Caixa getCaixa() {
        return caixa;
    }

    public void setCaixa(Caixa caixa) {
        this.caixa = caixa;
    }
    
    public JLabel getJLabel() {
        return jlabel;
    }

    public boolean isEmUso() {
        return emUso;
    }

    public int getImagemCliente() {
        return imagemCliente;
    }

    public void setImagemCliente(int imagemCliente) {
        this.imagemCliente = imagemCliente;
    }
    
    void imagem(int numero){
        switch(numero){
            case 1:
                getJLabel().setIcon(new javax.swing.ImageIcon(getClass().getResource("/br/ifce/so/projeto/display/imagens/clienteAndando1a.png")));
                break;
            case 2:
                getJLabel().setIcon(new javax.swing.ImageIcon(getClass().getResource("/br/ifce/so/projeto/display/imagens/clienteAndando1b.png")));
                break;
            case 3:
                getJLabel().setIcon(new javax.swing.ImageIcon(getClass().getResource("/br/ifce/so/projeto/display/imagens/clienteAndando1c.png")));
                break;
            case 4:
                getJLabel().setIcon(new javax.swing.ImageIcon(getClass().getResource("/br/ifce/so/projeto/display/imagens/ClienteDescendo1.png")));
                break; 
            case 5:
                getJLabel().setIcon(new javax.swing.ImageIcon(getClass().getResource("/br/ifce/so/projeto/display/imagens/ClienteSubindo1.png")));
                break; 
        }
    }
    
    public void dorme(int tempo){
        try {
                sleep(tempo);
        }
        catch (InterruptedException ex) {
                
        }
    }
    
    public void andaEixoX(int inicio, int fim, int tempo, int passo){
        int x = inicio;
        int y =  getJLabel().getLocation().y;
        while(x <= fim){
            for(int i = 1; i <=3; i++){
                getJLabel().setLocation(x, y);
                imagem(i);
                dorme(tempo);
                x += passo;
            }
        }
    }
        
    public void andaEixoY(int inicio, int fim, int tempo, int passo){
        int x =  getJLabel().getLocation().x;
        int y = inicio;
        if(passo > 0){
            while(y <= fim){
                getJLabel().setLocation(x, y);
                imagem(4);
                dorme(tempo);
                y += passo;
                }
        }
        if(passo < 0){
            while(y >= fim){
                getJLabel().setLocation(x, y);
                imagem(5);
                dorme(tempo);
                y += passo;
            }
        }
        
    }
    
    public void chegaCliente(){
        andaEixoX(10, caixa.getPosicao_X(), 60, 8);
        andaEixoY(510, 380, 25, -8);
        System.out.println("x: " +getJLabel().getLocation().x+ "Y: " +getJLabel().getLocation().y) ;
    }
    
    public void vaiEmboraCliente(){
        andaEixoY(getJLabel().getLocation().y, 510, 25, 8);
        andaEixoX(getJLabel().getLocation().x, 1010, 60, 8);
        getJLabel().setVisible(false);
    }

    public void recebeDinheiro(){
        int a = 1;
        
        
        for(int h= 0; h<tempo; h++){
            imagem(5);
            for(int i = 0; i<100000; i++)
                for(int j= 0; j<10000;j++)
                    a = 2*a;
            for(int i = 0; i<100000; i++)
                for(int j= 0; j<10000;j++)
                    a = 2*a;
        }
        imagem(4);
    }
}
