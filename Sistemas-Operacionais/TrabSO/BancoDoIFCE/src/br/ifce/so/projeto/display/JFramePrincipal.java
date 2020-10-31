/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package br.ifce.so.projeto.display;

import br.ifce.so.projeto.Caixa;
import br.ifce.so.projeto.Cliente;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.Semaphore;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JLabel;
import javax.swing.JOptionPane;

/**
 *
 * @author Nonato Dias
 */
public class JFramePrincipal extends javax.swing.JFrame {
    
    static int caixas;
    private int senha;
    private int tempoDeAtendimento;
    private static int senhaDaVez;
    
    public JFramePrincipal.ThreadCaixa tCaixa01;
    public JFramePrincipal.ThreadCaixa tCaixa02;
    public JFramePrincipal.ThreadCaixa tCaixa03;
    public JFramePrincipal.ThreadCaixa tCaixa04;
    public JFramePrincipal.ThreadCaixa tCaixa05;
    
    public Caixa caixa01;
    public Caixa caixa02;
    public Caixa caixa03;
    public Caixa caixa04;
    public Caixa caixa05;
    
    public static Semaphore semaphore_caixa;
    public static Semaphore semaphore_cliente;
    public static Semaphore semaphore_mutex;
    
    public static Semaphore semaphore_Log;
    
    public static Semaphore semaphore_CaixaLivre;
    public static int numeroDeCaixas;
    
    public List<Cliente> clientes;
    public List<Caixa> ListaDeCaixasLivres;
   
    
    /**
     * Creates new form JFramePrincipal
     */
    public JFramePrincipal() {
        initComponents();

        senha = 1;
        senhaDaVez = 0;
        tempoDeAtendimento = 0;
        clientes = new ArrayList<>();
        ListaDeCaixasLivres = new ArrayList<>();
 
        semaphore_caixa = new Semaphore(0);
        semaphore_cliente = new Semaphore(0);
        semaphore_mutex = new Semaphore(1);
        semaphore_CaixaLivre = new Semaphore(1);
        semaphore_Log = new Semaphore(1);  
        
        
        caixa01 = new Caixa("caixa 01", 1, this.labelCaixa(200, 250), 218);
        caixa02 = new Caixa("caixa 02", 1, this.labelCaixa(380, 250), 410);
        caixa03 = new Caixa("caixa 03", 1, this.labelCaixa(550, 250), 578);
        caixa04 = new Caixa("caixa 04", 1, this.labelCaixa(720, 250), 746);
        caixa05 = new Caixa("caixa 05", 1, this.labelCaixa(900, 250), 914);
         
        tCaixa01 = new JFramePrincipal.ThreadCaixa(caixa01);
        tCaixa02 = new JFramePrincipal.ThreadCaixa(caixa02);
        tCaixa03 = new JFramePrincipal.ThreadCaixa(caixa03);
        tCaixa04 = new JFramePrincipal.ThreadCaixa(caixa04);
        tCaixa05 = new JFramePrincipal.ThreadCaixa(caixa05);
       
    }

     public void proximaSenha() {
        this.senha = getSenha() + 1;
    }
    
    public int getSenha() {
        return senha;
    }
    
    public final JLabel labelCaixa(int x, int y){
        JLabel jLabel = new JLabel();
        jLabel.setSize(135, 130);
        jLabel.setVisible(true);
        jLabel.setLocation(x, y);
        this.jLayeredPane.add(jLabel);
        this.jLayeredPane.moveToFront(jLabel);
        return jLabel;
    }
    
    public void adicionaCliente(int senha, int tempo){
       JLabel jLabel = new JLabel();
       jLabel.setSize(90, 140);
       jLabel.setVisible(true);
       jLabel.setLocation(20, 520);
       jLabel.setText("N° " + senha);
       jLabel.setHorizontalTextPosition(JLabel.CENTER);
       jLabel.setVerticalTextPosition(JLabel.BOTTOM);
       jLayeredPane.add(jLabel);
       jLayeredPane.moveToFront(jLabel); 
       this.clientes.add(new Cliente(jLabel, tempo, senha, caixa01));
    }

    public Cliente getProximoCliente(Caixa caixa) {
       if(senhaDaVez < senha){
            Cliente c = this.clientes.get(senhaDaVez);
            c.setCaixa(caixa);
            senhaDaVez = senhaDaVez +1;
            return c;
        }
        return null;
    }
    
    public Caixa proximoCaixaVazio(){
        return ListaDeCaixasLivres.get(0);
    }
    
    public Caixa ProximaThreadCliente(){
        try{    
            Cliente c = getProximoCliente(proximoCaixaVazio());
            new ThreadCliente(c).start();
        }catch(IndexOutOfBoundsException i){

        }
        return proximoCaixaVazio();
    } 

    public void alteraImagemFundo (JLabel jlabel, int caixas){
        switch(caixas){
            case 1:
                jlabel.setIcon(new javax.swing.ImageIcon(getClass().getResource("/br/ifce/so/projeto/display/imagens/caixa01.png")));
                break;
            case 2:
                jlabel.setIcon(new javax.swing.ImageIcon(getClass().getResource("/br/ifce/so/projeto/display/imagens/caixa02.png")));
                break;
            case 3:
                jlabel.setIcon(new javax.swing.ImageIcon(getClass().getResource("/br/ifce/so/projeto/display/imagens/caixa03.png")));
                break;
            case 4:
                jlabel.setIcon(new javax.swing.ImageIcon(getClass().getResource("/br/ifce/so/projeto/display/imagens/caixa04.png")));
                break;
            case 5:
                jlabel.setIcon(new javax.swing.ImageIcon(getClass().getResource("/br/ifce/so/projeto/display/imagens/caixa05.png")));
                break;
            default:
                jlabel.setIcon(new javax.swing.ImageIcon(getClass().getResource("/br/ifce/so/projeto/display/imagens/caixa01.png")));
                break;
        }
    }
    
    public void iniciaCaixas(int numero){
        switch(numero){
            case 1:
                tCaixa01.start();
                break;
            case 2:
                tCaixa01.start();
                tCaixa02.start();
                break;
            case 3:
                tCaixa01.start();
                tCaixa02.start();
                tCaixa03.start();
                break;
            case 4:
                tCaixa01.start();
                tCaixa02.start();
                tCaixa03.start();
                tCaixa04.start();
                break;
            case 5:
                tCaixa01.start();
                tCaixa02.start();
                tCaixa03.start();
                tCaixa04.start();
                tCaixa05.start();
                break; 
            default:
                System.exit(0);
        }
    }
    
    /************************************************************************/
    /*                          Thread dos clientes                         */
    /************************************************************************/
    
    public class ThreadCliente extends Thread{
        private final Cliente cliente;
        

        public ThreadCliente (Cliente cliente){
            this.cliente = cliente;
        }
        
        
        @Override
        public void run(){
            
            try {
                semaphore_CaixaLivre.acquire();
                    ListaDeCaixasLivres.remove(cliente.getCaixa());
                semaphore_CaixaLivre.release();
                
                semaphore_mutex.acquire();
                    cliente.chegaCliente();
                semaphore_mutex.release();
                
                semaphore_cliente.release();
                    cliente.recebeDinheiro();
                    //cliente.getJLabel().setIcon(new javax.swing.ImageIcon(getClass().getResource("/br/ifce/so/projeto/display/imagens/ClienteDescendo1.png")));
                semaphore_caixa.acquire();
                
                semaphore_mutex.acquire();
                    cliente.vaiEmboraCliente();
                semaphore_mutex.release();
 
                semaphore_Log.acquire();
                    jTextAreaLogEventos.setText(jTextAreaLogEventos.getText()+"                   cliente: " + cliente.getSenha()+ " foi FINALIZADO \n");
                semaphore_Log.release();
            } catch (InterruptedException ex) {
                Logger.getLogger(JFramePrincipal.class.getName()).log(Level.SEVERE, null, ex);
            }
            
        }
        
    }//Final da classe ThreadCliente
    
    
    /************************************************************************/
    /*                          Thread dos caixas                           */
    /************************************************************************/
    
    public class ThreadCaixa extends Thread{
        private final Caixa caixaDaThread;

        public ThreadCaixa(Caixa caixa) {
            this.caixaDaThread = caixa;
        }

        public Caixa getCaixaDaThread() {
            return caixaDaThread;
        }
        
        @Override
        public void run(){
            try {
                while(true){
                    
                    semaphore_CaixaLivre.acquire();
                        ListaDeCaixasLivres.add(this.caixaDaThread);
                    semaphore_CaixaLivre.release();
                    
                    semaphore_cliente.acquire();
                        caixaDaThread.movimentaDinheiro(tempoDeAtendimento);
                    semaphore_caixa.release(); 
                    
                    semaphore_Log.acquire();
                        jTextAreaLogEventos.setText(jTextAreaLogEventos.getText()+"             " + caixaDaThread.getNome()+ " está LIVRE \n");
                    semaphore_Log.release();
                }
            } catch (InterruptedException ex) {
                Logger.getLogger(JFramePrincipal.class.getName()).log(Level.SEVERE, null, ex);
            }
        }
        
    }//Final da Classe ThreadCaixa
    
    
    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jLayeredPane = new javax.swing.JLayeredPane();
        jLabelPlanoDeFundo = new javax.swing.JLabel();
        jLabelTempoAtendimento = new javax.swing.JLabel();
        jTextFieldTempoAtendimento = new javax.swing.JTextField();
        jLabelSenha = new javax.swing.JLabel();
        jTextFieldSenha = new javax.swing.JTextField();
        jButtonInserirCliente = new javax.swing.JButton();
        jScrollPane1 = new javax.swing.JScrollPane();
        jTextAreaLogEventos = new javax.swing.JTextArea();
        jLabelLog = new javax.swing.JLabel();
        jLabelSenha1 = new javax.swing.JLabel();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setTitle("Banco do IFCE");
        setResizable(false);

        jLabelPlanoDeFundo.setIcon(new javax.swing.ImageIcon(getClass().getResource("/br/ifce/so/projeto/display/imagens/caixa05.png"))); // NOI18N

        jLabelTempoAtendimento.setFont(new java.awt.Font("Trebuchet MS", 0, 24)); // NOI18N
        jLabelTempoAtendimento.setText("Tempo de Atendimento:");

        jTextFieldTempoAtendimento.setFont(new java.awt.Font("Trebuchet MS", 0, 24)); // NOI18N
        jTextFieldTempoAtendimento.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jTextFieldTempoAtendimentoActionPerformed(evt);
            }
        });

        jLabelSenha.setFont(new java.awt.Font("Trebuchet MS", 0, 24)); // NOI18N
        jLabelSenha.setText(" Senha:");

        jTextFieldSenha.setEditable(false);
        jTextFieldSenha.setFont(new java.awt.Font("Trebuchet MS", 0, 24)); // NOI18N
        jTextFieldSenha.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                jTextFieldSenhaMouseClicked(evt);
            }
        });
        jTextFieldSenha.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jTextFieldSenhaActionPerformed(evt);
            }
        });

        jButtonInserirCliente.setFont(new java.awt.Font("Tahoma", 0, 18)); // NOI18N
        jButtonInserirCliente.setText("Inserir Cliente");
        jButtonInserirCliente.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButtonInserirClienteActionPerformed(evt);
            }
        });

        jTextAreaLogEventos.setEditable(false);
        jTextAreaLogEventos.setColumns(20);
        jTextAreaLogEventos.setRows(5);
        jScrollPane1.setViewportView(jTextAreaLogEventos);

        jLabelLog.setBackground(new java.awt.Color(0, 0, 0));
        jLabelLog.setFont(new java.awt.Font("Tahoma", 1, 18)); // NOI18N
        jLabelLog.setForeground(new java.awt.Color(255, 255, 255));
        jLabelLog.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        jLabelLog.setText("LOG DE EVENTOS");
        jLabelLog.setBorder(javax.swing.BorderFactory.createLineBorder(new java.awt.Color(0, 0, 0)));
        jLabelLog.setOpaque(true);

        jLabelSenha1.setFont(new java.awt.Font("Trebuchet MS", 0, 24)); // NOI18N
        jLabelSenha1.setText("Segundos");

        jLayeredPane.setLayer(jLabelPlanoDeFundo, javax.swing.JLayeredPane.DEFAULT_LAYER);
        jLayeredPane.setLayer(jLabelTempoAtendimento, javax.swing.JLayeredPane.DEFAULT_LAYER);
        jLayeredPane.setLayer(jTextFieldTempoAtendimento, javax.swing.JLayeredPane.DEFAULT_LAYER);
        jLayeredPane.setLayer(jLabelSenha, javax.swing.JLayeredPane.DEFAULT_LAYER);
        jLayeredPane.setLayer(jTextFieldSenha, javax.swing.JLayeredPane.DEFAULT_LAYER);
        jLayeredPane.setLayer(jButtonInserirCliente, javax.swing.JLayeredPane.DEFAULT_LAYER);
        jLayeredPane.setLayer(jScrollPane1, javax.swing.JLayeredPane.DEFAULT_LAYER);
        jLayeredPane.setLayer(jLabelLog, javax.swing.JLayeredPane.DEFAULT_LAYER);
        jLayeredPane.setLayer(jLabelSenha1, javax.swing.JLayeredPane.DEFAULT_LAYER);

        javax.swing.GroupLayout jLayeredPaneLayout = new javax.swing.GroupLayout(jLayeredPane);
        jLayeredPane.setLayout(jLayeredPaneLayout);
        jLayeredPaneLayout.setHorizontalGroup(
            jLayeredPaneLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jLayeredPaneLayout.createSequentialGroup()
                .addGap(479, 479, 479)
                .addComponent(jLabelSenha1, javax.swing.GroupLayout.PREFERRED_SIZE, 109, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(845, Short.MAX_VALUE))
            .addGroup(jLayeredPaneLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                .addGroup(jLayeredPaneLayout.createSequentialGroup()
                    .addGap(0, 0, Short.MAX_VALUE)
                    .addGroup(jLayeredPaneLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                        .addComponent(jLabelPlanoDeFundo, javax.swing.GroupLayout.PREFERRED_SIZE, 1120, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGroup(jLayeredPaneLayout.createSequentialGroup()
                            .addGap(20, 20, 20)
                            .addComponent(jLabelTempoAtendimento, javax.swing.GroupLayout.PREFERRED_SIZE, 272, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                            .addComponent(jTextFieldTempoAtendimento, javax.swing.GroupLayout.PREFERRED_SIZE, 166, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addGap(207, 207, 207)
                            .addComponent(jLabelSenha, javax.swing.GroupLayout.PREFERRED_SIZE, 90, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addGap(0, 0, 0)
                            .addComponent(jTextFieldSenha, javax.swing.GroupLayout.PREFERRED_SIZE, 100, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addGap(20, 20, 20)
                            .addComponent(jButtonInserirCliente, javax.swing.GroupLayout.PREFERRED_SIZE, 220, javax.swing.GroupLayout.PREFERRED_SIZE)))
                    .addGroup(jLayeredPaneLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                        .addComponent(jLabelLog, javax.swing.GroupLayout.PREFERRED_SIZE, 300, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 300, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGap(0, 0, Short.MAX_VALUE)))
        );
        jLayeredPaneLayout.setVerticalGroup(
            jLayeredPaneLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jLayeredPaneLayout.createSequentialGroup()
                .addContainerGap(678, Short.MAX_VALUE)
                .addComponent(jLabelSenha1, javax.swing.GroupLayout.PREFERRED_SIZE, 30, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(22, 22, 22))
            .addGroup(jLayeredPaneLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                .addGroup(jLayeredPaneLayout.createSequentialGroup()
                    .addGap(0, 0, Short.MAX_VALUE)
                    .addGroup(jLayeredPaneLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                        .addGroup(jLayeredPaneLayout.createSequentialGroup()
                            .addComponent(jLabelPlanoDeFundo, javax.swing.GroupLayout.PREFERRED_SIZE, 650, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addGap(20, 20, 20)
                            .addGroup(jLayeredPaneLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                .addComponent(jLabelTempoAtendimento, javax.swing.GroupLayout.PREFERRED_SIZE, 30, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addComponent(jTextFieldTempoAtendimento, javax.swing.GroupLayout.PREFERRED_SIZE, 30, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addComponent(jLabelSenha, javax.swing.GroupLayout.PREFERRED_SIZE, 30, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addComponent(jTextFieldSenha, javax.swing.GroupLayout.PREFERRED_SIZE, 30, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addComponent(jButtonInserirCliente, javax.swing.GroupLayout.PREFERRED_SIZE, 30, javax.swing.GroupLayout.PREFERRED_SIZE)))
                        .addGroup(jLayeredPaneLayout.createSequentialGroup()
                            .addComponent(jLabelLog, javax.swing.GroupLayout.PREFERRED_SIZE, 40, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addGap(0, 0, 0)
                            .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 670, javax.swing.GroupLayout.PREFERRED_SIZE)))
                    .addGap(0, 0, Short.MAX_VALUE)))
        );

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jLayeredPane)
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jLayeredPane)
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void jTextFieldTempoAtendimentoActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jTextFieldTempoAtendimentoActionPerformed
    if(!ListaDeCaixasLivres.isEmpty()){
            try{
                tempoDeAtendimento = Integer.parseInt(jTextFieldTempoAtendimento.getText());
                adicionaCliente(getSenha(), tempoDeAtendimento);
                Caixa x = ProximaThreadCliente();
                
                semaphore_Log.acquire();
                    jTextAreaLogEventos.setText(jTextAreaLogEventos.getText()+"Cliente"+ " "+getSenha()+" inserido com "+tempoDeAtendimento+"s no "+ x.getNome()+" \n");
                    jTextFieldSenha.setText(""+getSenha());
                semaphore_Log.release();
                
                proximaSenha();

            }catch(NumberFormatException e){
                JOptionPane.showMessageDialog(null, "Digite um numero inteiro em segundos ","TEMPO DE ATENDIMENTO INCORRETO", JOptionPane.ERROR_MESSAGE);
                jTextFieldTempoAtendimento.setText(null);
            } catch (InterruptedException ex) { 
               Logger.getLogger(JFramePrincipal.class.getName()).log(Level.SEVERE, null, ex);
           } 
       }else{
           JOptionPane.showMessageDialog(null, "Aguarde a liberacao de um caixa ","CAIXAS OCUPADOS", JOptionPane.INFORMATION_MESSAGE);
       }
    }//GEN-LAST:event_jTextFieldTempoAtendimentoActionPerformed

    private void jTextFieldSenhaMouseClicked(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_jTextFieldSenhaMouseClicked
        // TODO add your handling code here:
        JOptionPane.showMessageDialog(null, "As senhas sao geradas automaticamente ","Atencao", JOptionPane.INFORMATION_MESSAGE);
    }//GEN-LAST:event_jTextFieldSenhaMouseClicked

    private void jTextFieldSenhaActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jTextFieldSenhaActionPerformed

    }//GEN-LAST:event_jTextFieldSenhaActionPerformed

    private void jButtonInserirClienteActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButtonInserirClienteActionPerformed
       if(!ListaDeCaixasLivres.isEmpty()){
            try{
                tempoDeAtendimento = Integer.parseInt(jTextFieldTempoAtendimento.getText());
                adicionaCliente(getSenha(), tempoDeAtendimento);
                Caixa x = ProximaThreadCliente();
                
                semaphore_Log.acquire();
                    jTextAreaLogEventos.setText(jTextAreaLogEventos.getText()+"Cliente"+ " "+getSenha()+" inserido com "+tempoDeAtendimento+"s no "+ x.getNome()+" \n");
                    jTextFieldSenha.setText(""+getSenha());
                semaphore_Log.release();
                
                proximaSenha();

            }catch(NumberFormatException e){
                JOptionPane.showMessageDialog(null, "Digite um numero inteiro em segundos ","TEMPO DE ATENDIMENTO INCORRETO", JOptionPane.ERROR_MESSAGE);
                jTextFieldTempoAtendimento.setText(null);
            } catch (InterruptedException ex) { 
               Logger.getLogger(JFramePrincipal.class.getName()).log(Level.SEVERE, null, ex);
           } 
       }else{
           JOptionPane.showMessageDialog(null, "Aguarde a liberacao de um caixa ","CAIXAS OCUPADOS", JOptionPane.INFORMATION_MESSAGE);
       }

    }//GEN-LAST:event_jButtonInserirClienteActionPerformed

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(JFramePrincipal.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(JFramePrincipal.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(JFramePrincipal.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(JFramePrincipal.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {

                JFramePrincipal displayPrincipal = new JFramePrincipal();
                displayPrincipal.setLocationRelativeTo(null);
                
                 DisplayInicio dInicio = new DisplayInicio(displayPrincipal, true);
                dInicio.setLocationRelativeTo(null);
                dInicio.setVisible(true);
                caixas = dInicio.getNumeroDeCaixas();
                displayPrincipal.alteraImagemFundo(displayPrincipal.jLabelPlanoDeFundo, caixas);
                displayPrincipal.iniciaCaixas(caixas);
                displayPrincipal.setVisible(true); 
                
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton jButtonInserirCliente;
    private javax.swing.JLabel jLabelLog;
    private javax.swing.JLabel jLabelPlanoDeFundo;
    private javax.swing.JLabel jLabelSenha;
    private javax.swing.JLabel jLabelSenha1;
    private javax.swing.JLabel jLabelTempoAtendimento;
    private javax.swing.JLayeredPane jLayeredPane;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JTextArea jTextAreaLogEventos;
    private javax.swing.JTextField jTextFieldSenha;
    private javax.swing.JTextField jTextFieldTempoAtendimento;
    // End of variables declaration//GEN-END:variables
}
