package view;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;

import org.omg.CORBA.Principal;

import controller.ExecPrincipal;
import controller.Main;
import model.DataIN;
import model.Estatistics;

import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.util.LinkedList;
import java.awt.event.ActionEvent;
import java.awt.Color;
import java.awt.SystemColor;
import java.awt.TextArea;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Label;

import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.SwingConstants;
import javax.swing.UIManager;
import javax.swing.JTextPane;
import javax.swing.JTextField;
import javax.swing.JTextArea;

public class Tela extends JFrame {

	private JPanel contentPane;
	private JTextField CilindroInicial;
	private JTextField QntCilindros;
	private JTextField seek;
	private JTextField nomeArquivo;
	private JTextField FCFS0;
	private JTextField FCFS1;
	private JTextField FCFS2;
	private JTextField FCFS3;
	private JTextField FCFS4;
	private JLabel label_2;
	private JLabel label_6;
	private JLabel label_7;
	private JLabel label_8;
	private JTextField SSF0;
	private JTextField SSF1;
	private JTextField SSF2;
	private JTextField SSF3;
	private JTextField SSF4;
	private JLabel label_9;
	private JTextField SCAN0;
	private JTextField SCAN1;
	private JTextField SCAN2;
	private JTextField SCAN3;
	private JTextField SCAN4;
	private JLabel label_10;
	private JTextField CSCAN0;
	private JTextField CSCAN1;
	private JTextField CSCAN2;
	private JTextField CSCAN3;
	private JTextField CSCAN4;
	private JButton Sair;
	private JLabel label_11;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Tela frame = new Tela();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public Tela() {
		setResizable(false);
		setTitle("HARD DISK ALGORITHMS");
		setName("HardDisk Algoritms");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 909, 447);
		contentPane = new JPanel();
		contentPane.setBackground(UIManager.getColor("Button.darkShadow"));
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);

		JButton btnNewButton = new JButton("Carregar Arquivo");
		btnNewButton.setFont(new Font("Tahoma", Font.PLAIN, 18));
		btnNewButton.setBackground(Color.LIGHT_GRAY);
		btnNewButton.setForeground(Color.BLACK);
		btnNewButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {					
				////dados de entrada
				if(QntCilindros.getText().isEmpty() || CilindroInicial.getText().isEmpty() || seek.getText().isEmpty())
					JOptionPane.showMessageDialog(null, "Entrada Inválida");
				else{
					int qntdCilinder = Integer.parseInt(QntCilindros.getText());
					int initialArmPosition = Integer.parseInt(CilindroInicial.getText());		
					Double seekTime = Double.parseDouble(seek.getText());
					LinkedList<Integer> Process = new LinkedList<>();
					try {
						Process = DataIN.getProcessArray();
					} catch (Exception e) {
						nomeArquivo.setText("Arquivo Inválido");
					}
					Configure configure = new Configure(qntdCilinder, initialArmPosition, seekTime, Process);
					System.out.println("validada");
					ExecPrincipal.principal(configure);
				}

				nomeArquivo.setText(Configure.nameFile);
				//sentando valores fcfs
				FCFS0.setText(Configure.results.removeFirst());
				FCFS1.setText(Configure.results.removeFirst());
				FCFS2.setText(Configure.results.removeFirst());
				FCFS3.setText(Configure.results.removeFirst());
				FCFS4.setText(Configure.results.removeFirst());

				//sentando valores ssf
				SSF0.setText(Configure.results.removeFirst());
				SSF1.setText(Configure.results.removeFirst());
				SSF2.setText(Configure.results.removeFirst());
				SSF3.setText(Configure.results.removeFirst());
				SSF4.setText(Configure.results.removeFirst());

				//setando valores scan
				SCAN0.setText(Configure.results.removeFirst());
				SCAN1.setText(Configure.results.removeFirst());
				SCAN2.setText(Configure.results.removeFirst());
				SCAN3.setText(Configure.results.removeFirst());
				SCAN4.setText(Configure.results.removeFirst());

				//setando valores cscan
				CSCAN0.setText(Configure.results.removeFirst());
				CSCAN1.setText(Configure.results.removeFirst());
				CSCAN2.setText(Configure.results.removeFirst());
				CSCAN3.setText(Configure.results.removeFirst());
				CSCAN4.setText(Configure.results.removeFirst());			

			}
		});
		btnNewButton.setBounds(10, 11, 167, 32);
		contentPane.add(btnNewButton);

		CilindroInicial = new JTextField();
		CilindroInicial.setFont(new Font("Tahoma", Font.PLAIN, 16));
		CilindroInicial.setBounds(10, 200, 167, 38);
		contentPane.add(CilindroInicial);
		CilindroInicial.setColumns(10);

		JLabel label = new JLabel("Cilindro Inicial");
		label.setFont(new Font("Tahoma", Font.PLAIN, 16));
		label.setBackground(SystemColor.menu);
		label.setBounds(10, 168, 211, 32);
		contentPane.add(label);

		QntCilindros = new JTextField();
		QntCilindros.setFont(new Font("Tahoma", Font.PLAIN, 16));
		QntCilindros.setColumns(10);
		QntCilindros.setBounds(10, 109, 167, 38);
		contentPane.add(QntCilindros);

		JLabel label_1 = new JLabel("Deslocamento Total");
		label_1.setFont(new Font("Tahoma", Font.PLAIN, 16));
		label_1.setHorizontalAlignment(SwingConstants.RIGHT);
		label_1.setBackground(SystemColor.menu);
		label_1.setBounds(187, 96, 156, 32);
		contentPane.add(label_1);

		seek = new JTextField();
		seek.setFont(new Font("Tahoma", Font.PLAIN, 16));
		seek.setColumns(10);
		seek.setBounds(10, 301, 167, 38);
		contentPane.add(seek);

		JLabel tempoSeek = new JLabel("Seek Time");
		tempoSeek.setFont(new Font("Tahoma", Font.PLAIN, 16));
		tempoSeek.setBackground(SystemColor.menu);
		tempoSeek.setBounds(10, 254, 211, 32);
		contentPane.add(tempoSeek);

		nomeArquivo = new JTextField();
		nomeArquivo.setBounds(187, 11, 686, 32);
		contentPane.add(nomeArquivo);
		nomeArquivo.setColumns(10);

		FCFS0 = new JTextField();
		FCFS0.setFont(new Font("Tahoma", Font.PLAIN, 16));
		FCFS0.setBounds(349, 94, 123, 37);
		contentPane.add(FCFS0);
		FCFS0.setColumns(10);

		FCFS1 = new JTextField();
		FCFS1.setFont(new Font("Tahoma", Font.PLAIN, 16));
		FCFS1.setColumns(10);
		FCFS1.setBounds(349, 148, 123, 37);
		contentPane.add(FCFS1);

		FCFS2 = new JTextField();
		FCFS2.setFont(new Font("Tahoma", Font.PLAIN, 16));
		FCFS2.setColumns(10);
		FCFS2.setBounds(349, 201, 123, 37);
		contentPane.add(FCFS2);

		FCFS3 = new JTextField();
		FCFS3.setFont(new Font("Tahoma", Font.PLAIN, 16));
		FCFS3.setColumns(10);
		FCFS3.setBounds(349, 254, 123, 37);
		contentPane.add(FCFS3);

		FCFS4 = new JTextField();
		FCFS4.setFont(new Font("Tahoma", Font.PLAIN, 16));
		FCFS4.setColumns(10);
		FCFS4.setBounds(349, 302, 123, 37);
		contentPane.add(FCFS4);

		label_2 = new JLabel("FCFS");
		label_2.setFont(new Font("Tahoma", Font.PLAIN, 16));
		label_2.setHorizontalAlignment(SwingConstants.CENTER);
		label_2.setBackground(SystemColor.menu);
		label_2.setBounds(349, 54, 123, 32);
		contentPane.add(label_2);

		JLabel label_3 = new JLabel("criado Andr\u00E9 Vieira da Silva");
		label_3.setFont(new Font("Tahoma", Font.PLAIN, 16));
		label_3.setBackground(SystemColor.menu);
		label_3.setBounds(10, 375, 211, 32);
		contentPane.add(label_3);

		JLabel label_4 = new JLabel("Deslocamento Medio");
		label_4.setFont(new Font("Tahoma", Font.PLAIN, 16));
		label_4.setHorizontalAlignment(SwingConstants.RIGHT);
		label_4.setBackground(SystemColor.menu);
		label_4.setBounds(187, 151, 156, 32);
		contentPane.add(label_4);

		JLabel label_5 = new JLabel("Deslocamento Medio");
		label_5.setFont(new Font("Tahoma", Font.PLAIN, 16));
		label_5.setHorizontalAlignment(SwingConstants.RIGHT);
		label_5.setBackground(SystemColor.menu);
		label_5.setBounds(187, 203, 156, 32);
		contentPane.add(label_5);

		label_6 = new JLabel("Variancia");
		label_6.setFont(new Font("Tahoma", Font.PLAIN, 16));
		label_6.setHorizontalAlignment(SwingConstants.RIGHT);
		label_6.setBackground(SystemColor.menu);
		label_6.setBounds(187, 257, 156, 32);
		contentPane.add(label_6);

		label_7 = new JLabel("Desvio Padr\u00E3o");
		label_7.setFont(new Font("Tahoma", Font.PLAIN, 16));
		label_7.setHorizontalAlignment(SwingConstants.RIGHT);
		label_7.setBackground(SystemColor.menu);
		label_7.setBounds(187, 307, 156, 32);
		contentPane.add(label_7);

		label_8 = new JLabel("SSF");
		label_8.setFont(new Font("Tahoma", Font.PLAIN, 16));
		label_8.setHorizontalAlignment(SwingConstants.CENTER);
		label_8.setBackground(SystemColor.menu);
		label_8.setBounds(482, 54, 123, 32);
		contentPane.add(label_8);

		SSF0 = new JTextField();
		SSF0.setFont(new Font("Tahoma", Font.PLAIN, 16));
		SSF0.setColumns(10);
		SSF0.setBounds(482, 94, 123, 37);
		contentPane.add(SSF0);

		SSF1 = new JTextField();
		SSF1.setFont(new Font("Tahoma", Font.PLAIN, 16));
		SSF1.setColumns(10);
		SSF1.setBounds(482, 148, 123, 37);
		contentPane.add(SSF1);

		SSF2 = new JTextField();
		SSF2.setFont(new Font("Tahoma", Font.PLAIN, 16));
		SSF2.setColumns(10);
		SSF2.setBounds(482, 201, 123, 37);
		contentPane.add(SSF2);

		SSF3 = new JTextField();
		SSF3.setFont(new Font("Tahoma", Font.PLAIN, 16));
		SSF3.setColumns(10);
		SSF3.setBounds(482, 254, 123, 37);
		contentPane.add(SSF3);

		SSF4 = new JTextField();
		SSF4.setFont(new Font("Tahoma", Font.PLAIN, 16));
		SSF4.setColumns(10);
		SSF4.setBounds(482, 302, 123, 37);
		contentPane.add(SSF4);

		label_9 = new JLabel("SCAN");
		label_9.setFont(new Font("Tahoma", Font.PLAIN, 16));
		label_9.setHorizontalAlignment(SwingConstants.CENTER);
		label_9.setBackground(SystemColor.menu);
		label_9.setBounds(615, 54, 123, 32);
		contentPane.add(label_9);

		SCAN0 = new JTextField();
		SCAN0.setFont(new Font("Tahoma", Font.PLAIN, 16));
		SCAN0.setColumns(10);
		SCAN0.setBounds(615, 94, 123, 37);
		contentPane.add(SCAN0);

		SCAN1 = new JTextField();
		SCAN1.setFont(new Font("Tahoma", Font.PLAIN, 16));
		SCAN1.setColumns(10);
		SCAN1.setBounds(615, 148, 123, 37);
		contentPane.add(SCAN1);

		SCAN2 = new JTextField();
		SCAN2.setFont(new Font("Tahoma", Font.PLAIN, 16));
		SCAN2.setColumns(10);
		SCAN2.setBounds(615, 201, 123, 37);
		contentPane.add(SCAN2);

		SCAN3 = new JTextField();
		SCAN3.setFont(new Font("Tahoma", Font.PLAIN, 16));
		SCAN3.setColumns(10);
		SCAN3.setBounds(615, 254, 123, 37);
		contentPane.add(SCAN3);

		SCAN4 = new JTextField();
		SCAN4.setFont(new Font("Tahoma", Font.PLAIN, 16));
		SCAN4.setColumns(10);
		SCAN4.setBounds(615, 302, 123, 37);
		contentPane.add(SCAN4);

		label_10 = new JLabel("C-SCAN");
		label_10.setFont(new Font("Tahoma", Font.PLAIN, 16));
		label_10.setHorizontalAlignment(SwingConstants.CENTER);
		label_10.setBackground(SystemColor.menu);
		label_10.setBounds(752, 54, 123, 32);
		contentPane.add(label_10);

		CSCAN0 = new JTextField();
		CSCAN0.setFont(new Font("Tahoma", Font.PLAIN, 16));
		CSCAN0.setColumns(10);
		CSCAN0.setBounds(752, 94, 123, 37);
		contentPane.add(CSCAN0);

		CSCAN1 = new JTextField();
		CSCAN1.setFont(new Font("Tahoma", Font.PLAIN, 16));
		CSCAN1.setColumns(10);
		CSCAN1.setBounds(752, 148, 123, 37);
		contentPane.add(CSCAN1);

		CSCAN2 = new JTextField();
		CSCAN2.setFont(new Font("Tahoma", Font.PLAIN, 16));
		CSCAN2.setColumns(10);
		CSCAN2.setBounds(752, 201, 123, 37);
		contentPane.add(CSCAN2);

		CSCAN3 = new JTextField();
		CSCAN3.setFont(new Font("Tahoma", Font.PLAIN, 16));
		CSCAN3.setColumns(10);
		CSCAN3.setBounds(752, 254, 123, 37);
		contentPane.add(CSCAN3);

		CSCAN4 = new JTextField();
		CSCAN4.setFont(new Font("Tahoma", Font.PLAIN, 16));
		CSCAN4.setColumns(10);
		CSCAN4.setBounds(752, 302, 123, 37);
		contentPane.add(CSCAN4);
		
		Sair = new JButton("Sair");
		Sair.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				System.exit(0);
			}
		});
		Sair.setBounds(752, 365, 121, 32);
		contentPane.add(Sair);
		
		label_11 = new JLabel("Quantidade Cilindros");
		label_11.setFont(new Font("Tahoma", Font.PLAIN, 16));
		label_11.setBackground(SystemColor.menu);
		label_11.setBounds(10, 66, 211, 32);
		contentPane.add(label_11);
	}
}
