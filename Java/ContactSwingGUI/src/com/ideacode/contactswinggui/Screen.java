package com.ideacode.contactswinggui;

import javax.swing.*;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;
import java.awt.desktop.PreferencesHandler;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;

public class Screen extends JFrame {
    private JPanel panelTop;
    private JPanel panelLeft;
    private JPanel panelRight;
    private JList listPeople;
    private JButton buttonNew;
    private JButton buttonSave;
    private JTextField textDateOfBirth;
    private JPanel panelMain;
    private JTextField textName;
    private JTextField textEmail;
    private JTextField textPhoneNumber;
    private JTextField textAddress;
    private JLabel labelAge;
    private ArrayList<Person> people;
    private DefaultListModel listPeopleModel;

    Screen(){
        super("My fancy contacts project");
        this.setContentPane(this.panelMain);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.pack();
        people = new ArrayList<Person>();
        listPeopleModel = new DefaultListModel();
        listPeople.setModel(listPeopleModel);
        buttonSave.setEnabled(false);

        buttonNew.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                buttonNewClick(e);
            }
        });

        buttonSave.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                buttonSaveClick(e);
            }
        });

        listPeople.addListSelectionListener(new ListSelectionListener() {
            @Override
            public void valueChanged(ListSelectionEvent e) {
                listPeopleSelection(e);
            }
        });
    }

    public void buttonNewClick(ActionEvent e){
        Person p = new Person(
                textName.getText(),
                textEmail.getText(),
                textPhoneNumber.getText(),
                textDateOfBirth.getText()
        );
        people.add(p);
        refreshPeopleList();
    }

    public void buttonSaveClick(ActionEvent e){
        int personNumber = listPeople.getSelectedIndex();
        if (personNumber >= 0) {
            Person p = people.get(personNumber);
            p.setName(textName.getText());
            p.setEmail(textName.getText());
            p.setPhoneNumber(textPhoneNumber.getText());
            p.setDateOfBirth(textDateOfBirth.getText());
            refreshPeopleList();
        }
    }

    public void listPeopleSelection(ListSelectionEvent e){
        int personNumber = listPeople.getSelectedIndex();
        if (personNumber >= 0){
            Person p = people.get(personNumber);
            textName.setText(p.getName());
            textEmail.setText(p.getEmail());
            textPhoneNumber.setText(p.getPhoneNumber());
            textDateOfBirth.setText(p.getDateOfBirth().format(DateTimeFormatter.ofPattern("dd/MM/yyyy")));
            labelAge.setText(Integer.toString(p.getAge()) + " years");
            buttonSave.setEnabled(true);
        } else {
            buttonSave.setEnabled(false);
        }
    }

    public void refreshPeopleList(){
        listPeopleModel.removeAllElements();
        System.out.println("Removing all people from list");
        for (Person p : people){
            System.out.println("Adding person to list: "+p.getName());
            listPeopleModel.addElement(p.getName());
        }
    }

    public void addPerson(Person p){
        people.add(p);
        refreshPeopleList();
    }

    public static void main(String[] args) {
        Screen screen = new Screen();
        screen.setVisible(true);

        Person sheldon = new Person("Sheldon Lee Cooper","sheldon@gmail.com","555 0001","26/02/1980");
        Person howard = new Person("Howard Joel Wolowitz","howard@gmail.com","555 0002","01/03/1981");
        Person raj = new Person("Rajesh Ramayan Koothrappali","raj@gmail.com","555 0003","06/10/1981");

        screen.addPerson(sheldon);
        screen.addPerson(howard);
        screen.addPerson(raj);
    }

    private void createUIComponents() {
        // TODO: place custom component creation code here
    }
}
