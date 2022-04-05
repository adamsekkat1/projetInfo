import java.util.*;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.Random;

public enum Artefact {
	aucun, eau, feu, air, terre, heliport
}

public enum CleArtefact {
	eau, feu, air, terre
}

public enum EtatZone {
	normale, inondee, submergee
}

interface Observer {
    public void update();
}

abstract class Observable {
    private ArrayList<Observer> observers;
    public Observable() {
	this.observers = new ArrayList<Observer>();
    }
    public void addObserver(Observer o) {
	observers.add(o);
    }
    public void notifyObservers() {
	for(Observer o : observers) {
	    o.update();
	}
    }
}




public class IleInterdite {
	public static void main(String[] args) {
	EventQueue.invokeLater(() -> {
	                CModele modele = new CModele();
	                CVue vue = new CVue(modele);
	 	});
	}
}



class CModele extends Observable {
    public static final int HAUTEUR=8, LARGEUR=8;
    private Zone[][] zones;
    public ArrayList<Joueur> joueurs;
    public ArrayList<Artefact> artefacts;
    public ArrayList<CleArtefact> cles;
    private int joueurActuel;
    private int nbActions;
    public int nbsubmergees;
    public boolean artefactSubmerge;
    public Zone posHeliport;
    
    public CModele() {
	zones = new Zone[LARGEUR][HAUTEUR];
	for(int i=0; i<LARGEUR; i++) {
	    for(int j=0; j<HAUTEUR; j++) {
		zones[i][j] = new Zone(this,i, j);
	    }
	}
	artefactSubmerge = false;
	joueurs = new ArrayList<Joueur>();
	joueurActuel = 0;
	nbActions = 0;
	artefacts = new ArrayList<Artefact>();
	cles = new ArrayList<CleArtefact>();
	
	System.out.println("Position des artefacts :");
	System.out.println("");
	
	init();
	
	System.out.println("");
	Random rand = new Random();
	
	
	int x = rand.nextInt(LARGEUR);
	int y = rand.nextInt(HAUTEUR);
	ajouteJoueur(Color.PINK, "Joueur 1",this.getZone(x, y));
	
	x = rand.nextInt(LARGEUR);
	y = rand.nextInt(HAUTEUR);
	ajouteJoueur(Color.RED, "Joueur 2",this.getZone(x, y));
	
	x = rand.nextInt(LARGEUR);
	y = rand.nextInt(HAUTEUR);
	ajouteJoueur(Color.GREEN, "Joueur 3",this.getZone(x, y));
	
	
	System.out.println("");
	Joueur j = joueurs.get(joueurActuel);
	System.out.println("C'est au tour de "+j.getNom()+", situé sur la case ("+j.getPos().getX()+","+j.getPos().getY()+") de jouer !");
	
    }
    
    public void init() {
    	this.nbsubmergees = 0;
    	Random rand = new Random();
    	for(int i=0; i<5; i++) {
	    	
	    	int x,y;
	    	do {
	    		x = rand.nextInt(LARGEUR);
	    		y = rand.nextInt(HAUTEUR);
	    	}
	    	while (getZone(x,y).getArtefact()!=Artefact.aucun);	// J'ai choisi cette manière de choisir des cases de façon aléatoire.
	    	switch(i) {
	    	case 0 : getZone(x,y).addArtefact(Artefact.feu); System.out.println("- feu : ("+x+","+y+")"); break;
	    	case 1 : getZone(x,y).addArtefact(Artefact.air); System.out.println("- air : ("+x+","+y+")"); break;
	    	case 2 : getZone(x,y).addArtefact(Artefact.eau); System.out.println("- eau : ("+x+","+y+")"); break;
	    	case 3 : getZone(x,y).addArtefact(Artefact.terre); System.out.println("- terre : ("+x+","+y+")"); break;
	    	case 4 : getZone(x,y).addArtefact(Artefact.heliport); System.out.println("Position de l'heliport : ("+x+","+y+")"); posHeliport = getZone(x,y); break;
	    	}
	} artefacts.add(Artefact.feu); artefacts.add(Artefact.air); artefacts.add(Artefact.eau); artefacts.add(Artefact.terre);
	cles.add(CleArtefact.feu); cles.add(CleArtefact.air); cles.add(CleArtefact.eau); cles.add(CleArtefact.terre);
    }
    
    public void ajouteJoueur(Color c, String name, Zone z) {
    	Joueur j = new Joueur(this,c,name,z);
    	joueurs.add(j);
    }
    
    
    public void inondation() {
    	Random rand = new Random();
    	for(int i=0; i<3; i++) {
    	if (nbsubmergees<HAUTEUR*LARGEUR) {
    	int x,y;
    	do {
    		x = rand.nextInt(LARGEUR);
    		y = rand.nextInt(HAUTEUR);
    	}
    	while (getZone(x,y).getEtat()==EtatZone.submergee);
    	getZone(x,y).inonder();
    	
    	System.out.println("zone : ("+x+","+y+") inondee");
    	
    	if(getZone(x,y).getEtat()==EtatZone.submergee) {
    		nbsubmergees++;
    		if(getZone(x,y).getArtefact()!=Artefact.aucun) {
    			
    			System.out.println("La partie est perdue car un artefact est submergé");
    			
    			artefactSubmerge = true;
    		}
    	}
    	}
    	}System.out.println("");
    }

    protected int compteVoisines(int x, int y) {
	int res=0;
	
	for(int i=x-1; i<=x+1; i++) {
	    for(int j=y-1; j<=y+1; j++) {
		if (zones[i][j].etat!=EtatZone.submergee) { res++; }
	    }
	}
	if (zones[x][y].etat!=EtatZone.submergee) { return res; }
	else { return res - 1;}
    }

    public Zone getZone(int x, int y) {
	return zones[x][y];
    }
    
    public int getJoueurActuel() {return joueurActuel;}
    
    public void effectueAction() {nbActions++;}
    
    public int getNbActions() {return nbActions;}
    
    public void nextPlayer() {
    	nbActions = 0;
    	if(joueurActuel<joueurs.size()-1) {
    		joueurActuel++;
    	}else {
    		joueurActuel = 0;
    	}
    }
    
    public void tuerJoueur(int i) {
    	System.out.println("Le joueur "+joueurs.get(i).getNom()+" est mort"); 
    	System.out.println("La partie est perdue");
    	joueurs.remove(i);
    }
}


class Joueur {
	private CModele modele;
	private ArrayList<Artefact> artefactsJ;
	private ArrayList<CleArtefact> clesJ;
	private String nom;
	private Color couleur;
	private Zone position;
	
	public Joueur(CModele modele, Color c, String name, Zone z) {
		this.modele = modele;
		this.artefactsJ = new ArrayList<Artefact>();
		this.clesJ = new ArrayList<CleArtefact>();
		this.nom = name;
		this.couleur = c;
		this.position = z;
		System.out.println("Nouveau Joueur "+name+" apparait sur la case ("+z.getX()+","+z.getY()+")");
	}
	public Zone getPos() {return this.position;}
	public String getNom() {return this.nom;}
	public Color getCouleur() {return this.couleur;}
	public void deplacementHaut() {
		System.out.print("Deplacement de "+nom+" de la case ("+this.position.getX()+","+this.position.getY()+") vers la case (");
		this.position = modele.getZone(this.position.getX(),this.position.getY()-1);
		System.out.println(this.position.getX()+","+this.position.getY()+")");
	}
	public void deplacementBas() {
		System.out.print("Deplacement de "+nom+" de la case ("+this.position.getX()+","+this.position.getY()+") vers la case (");
		this.position = modele.getZone(this.position.getX(),this.position.getY()+1);
		System.out.println(this.position.getX()+","+this.position.getY()+")");
	}
	public void deplacementGauche() {
		System.out.print("Deplacement de "+nom+" de la case ("+this.position.getX()+","+this.position.getY()+") vers la case (");
		this.position = modele.getZone(this.position.getX()-1,this.position.getY());
		System.out.println(this.position.getX()+","+this.position.getY()+")");
	}
	public void deplacementDroite() {
		System.out.print("Deplacement de "+nom+" de la case ("+this.position.getX()+","+this.position.getY()+") vers la case (");
		this.position = modele.getZone(this.position.getX()+1,this.position.getY());
		System.out.println(this.position.getX()+","+this.position.getY()+")");
	}
	public void chercheCle() {
		if(modele.cles.size()!=0) {
			Random rand = new Random();
			float obtientcle = rand.nextFloat();
			if(obtientcle < 0.8) {
				int alea = rand.nextInt(modele.cles.size());
				CleArtefact c= modele.cles.get(alea);
				this.addCle(c);		System.out.println("Le joueur "+this.nom+" a obtenu la clé "+c);
			}
		}
	}
	public void addCle(CleArtefact c) {
		modele.cles.remove(c);
		clesJ.add(c);
	}
	public ArrayList<Artefact> getArtefactsJ(){return artefactsJ;}
	public ArrayList<CleArtefact> getClesJ(){return clesJ;}
	
	
	public void addArtefact(Artefact a) {
		this.position.removeArtefact();
		modele.artefacts.remove(a);
		artefactsJ.add(a);
	}
	
	
	public void useCle(CleArtefact c) {
		clesJ.remove(c);
	}
	
	public void removeCle(CleArtefact c) {
		clesJ.remove(c);
		modele.cles.add(c);
	}
	
	public void donneCle(Joueur j) {
		CleArtefact c = this.clesJ.get(0);
		j.getClesJ().add(c);
		System.out.println("Le joueur "+this.getNom()+" donne sa cle de "+c+" au joueur "+j.getNom());
		this.useCle(c);
	}
}



class Zone {
    private CModele modele;
    
    protected EtatZone etat;
    protected Artefact artefact;

    private final int x, y;
    
    public Zone(CModele modele, int x, int y) {
        this.modele = modele;
        this.etat = EtatZone.normale;
        this.x = x; this.y = y;
        this.artefact = Artefact.aucun;
    }	
    
    
    public int getX() {return this.x;}
    public int getY() {return this.y;}
    public EtatZone getEtat() {return etat;}
    public void changeEtat(EtatZone e) {this.etat = e;}
    public Artefact getArtefact() {return this.artefact;}
    public void addArtefact(Artefact a) {this.artefact = a;}
    public void removeArtefact() {this.artefact = Artefact.aucun;}
    
    
    public void inonder() {
    	if (this.etat!=EtatZone.normale) {
    		this.changeEtat(EtatZone.submergee);
    	} else { this.changeEtat(EtatZone.inondee);}
    }
    
    public void assecher() {
    	if(this.etat==EtatZone.inondee) {
    		this.changeEtat(EtatZone.normale);
    	}
    }
    public boolean estTraversable() { return this.etat!=EtatZone.submergee;}
}

class CVue {
    private JFrame frame;
    private VueGrille grille;
    private VueCommandes commandes;

    public CVue(CModele modele) {
	frame = new JFrame();
	frame.setTitle("IleInterdite de Leacock");
	frame.setLayout(new FlowLayout());

	grille = new VueGrille(modele);
	frame.add(grille);
	commandes = new VueCommandes(modele);
	frame.add(commandes);
	frame.pack();
	frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	frame.setVisible(true);
    }
    
    public VueCommandes getVueCommandes() {return commandes;}
    
}

class VueGrille extends JPanel implements Observer {
    private CModele modele;
    private final static int TAILLE = 30;

    public VueGrille(CModele modele) {
    	this.modele = modele;
    	modele.addObserver(this);
    	Dimension dim = new Dimension(TAILLE*CModele.LARGEUR*3,
    			TAILLE*CModele.HAUTEUR*3);
    	this.setPreferredSize(dim);
    }

    public void update() { repaint(); }

    public void paintComponent(Graphics g) {
    	super.repaint();
    	for(int i=0; i<CModele.LARGEUR; i++) {
    		for(int j=0; j<CModele.HAUTEUR; j++) {
    			paint(g, modele.getZone(i, j), i*TAILLE*3, j*TAILLE*3);
    			paint2(g, modele.getZone(i, j), i*TAILLE*3 + TAILLE, j*TAILLE*3 + TAILLE);
    		}
    	}
    	for(int i=0; i<modele.joueurs.size(); i++) {
    		Zone pos = modele.joueurs.get(i).getPos();
		
    		paintJ(g, pos, pos.getX()*TAILLE*3 + TAILLE*15/12, pos.getY()*TAILLE*3 + TAILLE*3/2, modele.joueurs.get(i).getCouleur());
	}
	
	}
    private void paint(Graphics g, Zone zone, int x, int y) {
    	
    	if (zone.etat==EtatZone.normale) {g.setColor(Color.WHITE);}
    	else if (zone.etat==EtatZone.inondee) {g.setColor(Color.GRAY);}
    	else { g.setColor(Color.BLACK); }
	
	
    	g.fillRect(x, y, TAILLE*3, TAILLE*3);	// Les cases sont de taille : TAILLE*3 par TAILLE*3 pour faciliter les autres affichages
    	
}
    
    private void paint2(Graphics g, Zone zone, int x, int y) {

    	if(zone.getEtat()!=EtatZone.submergee) {
    	switch(zone.getArtefact()) {		// On affiche des artefacts de taille : TAILLE par TAILLE
    	case aucun : break;
    	case eau : g.setColor(Color.BLUE); break;
    	case feu : g.setColor(Color.RED); break;
    	case terre : g.setColor(Color.ORANGE); break;
    	case air : g.setColor(Color.CYAN); break;
    	case heliport : g.setColor(Color.GREEN);  break;
        }g.fillRect(x, y, TAILLE, TAILLE);
    }
}
    
    private void paintJ(Graphics g, Zone zone, int x, int y, Color c) {
    	g.setColor(c);
    	g.fillRect(x, y, TAILLE/2, TAILLE*3/2);	// La hauteur du joueur est 3 fois plus grande que sa largeur.
    }
}


class VueCommandes extends JPanel {
    private CModele modele;
    private JButton boutonHaut;
    private JButton boutonBas;
    private JButton boutonGauche;
    private JButton boutonDroite;
    private JButton finDeTour;
    private JButton assechHaut;
    private JButton assechBas;
    private JButton assechGauche;
    private JButton assechDroite;
    private JButton assechIci;
    private JButton deverouiller;
    private JButton donnerCle;
    private JButton passer;
    
    public VueCommandes(CModele modele) {
	this.modele = modele;
	
	Init();
    }
    
    public void Init() {
    	Controleur ctrl = new Controleur(modele, this);
    	
    	boutonGauche = new JButton("<");
    	this.add(boutonGauche);
    	boutonGauche.setActionCommand("Gauche");
    	boutonGauche.addActionListener(ctrl);

    	boutonHaut = new JButton("^");
    	this.add(boutonHaut);
    	boutonHaut.setActionCommand("Haut");
    	boutonHaut.addActionListener(ctrl);
    	
    	boutonBas = new JButton("v");
    	this.add(boutonBas);
    	boutonBas.addActionListener(ctrl);
    	boutonBas.setActionCommand("Bas");
    	
    	boutonDroite = new JButton(">");
    	this.add(boutonDroite);
    	boutonDroite.addActionListener(ctrl);
    	boutonDroite.setActionCommand("Droite");
    	
    	assechGauche = new JButton("Assecher <");
    	this.add(assechGauche);
    	assechGauche.addActionListener(ctrl);
    	assechGauche.setActionCommand("AssechGauche");
    	
    	assechHaut = new JButton("Assecher ^");
    	this.add(assechHaut);
    	assechHaut.addActionListener(ctrl);
    	assechHaut.setActionCommand("AssechHaut");
    	
    	assechBas= new JButton("Assecher v");
    	this.add(assechBas);
    	assechBas.addActionListener(ctrl);
    	assechBas.setActionCommand("AssechBas");
    	
    	assechDroite= new JButton("Assecher >");
    	this.add(assechDroite);
    	assechDroite.addActionListener(ctrl);
    	assechDroite.setActionCommand("AssechDroite");
    	
    	assechIci = new JButton("Assecher ici");
    	this.add(assechIci);
    	assechIci.addActionListener(ctrl);
    	assechIci.setActionCommand("AssechIci");
    	
    	deverouiller = new JButton("Deverouiller");
    	this.add(deverouiller);
    	deverouiller.addActionListener(ctrl);
    	deverouiller.setActionCommand("Unlock");
    	
    	donnerCle = new JButton("Donner Cle");
    	this.add(donnerCle);
    	donnerCle.addActionListener(ctrl);
    	donnerCle.setActionCommand("Donner");
    	
    	passer = new JButton("Passer");
    	this.add(passer);
    	passer.addActionListener(ctrl);
    	passer.setActionCommand("Passer");
    	
    	finDeTour = new JButton("Fin");
    	this.add(finDeTour);
    	finDeTour.addActionListener(ctrl);
    	finDeTour.setActionCommand("Tour");
    	finDeTour.setEnabled(false);
    	
    }
    
    public JButton getBoutonHaut() {return boutonHaut;}
    public JButton getBoutonBas() {return boutonBas;}
    public JButton getBoutonGauche() {return boutonGauche;}
    public JButton getBoutonDroite() {return boutonDroite;}
    public JButton getfinDeTour() {return finDeTour;}
    public JButton getAssechBas() {return assechBas;}
    public JButton getAssechGauche() {return assechGauche;}
    public JButton getAssechHaut() {return assechHaut;}
    public JButton getAssechDroite() {return assechDroite;}
    public JButton getAssechIci() {return assechIci;}
    public JButton getDeverouiller() {return deverouiller;}
    public JButton getEchange() {return donnerCle;}
    public JButton getPasser() {return passer;}
}

class Controleur implements ActionListener {
	public boolean partieTerminee;
    CModele modele;
    VueCommandes vue;
    public Controleur(CModele modele, VueCommandes vue) { this.modele = modele; this.vue = vue; this.partieTerminee=false;}
    public void actionPerformed(ActionEvent e) {
    	
    	if(modele.getNbActions() < 3 && !partieTerminee) {
    		
    		vue.getfinDeTour().setEnabled(false);
			Joueur j = modele.joueurs.get(modele.getJoueurActuel());
			
    		switch(e.getActionCommand()) {
    		
    		
    		case "Bas" : 
    			if(j.getPos().getY() < modele.HAUTEUR-1 && modele.getZone(j.getPos().getX(), j.getPos().getY()+1).estTraversable()) {
    				j.deplacementBas(); testVictoire();
    				modele.effectueAction();
    			} break;
    			
    			
    		case "Haut" :
    			if(j.getPos().getY() > 0 && modele.getZone(j.getPos().getX(), j.getPos().getY()-1).estTraversable()) {
    				j.deplacementHaut(); testVictoire();
    				modele.effectueAction(); 
    			} break;
    			
    			
    		case "Gauche" :
    			if(j.getPos().getX() > 0 && modele.getZone(j.getPos().getX()-1, j.getPos().getY()).estTraversable()) {
    				j.deplacementGauche(); testVictoire();
    				modele.effectueAction(); 
    			} break;
    			
    			
    		case "Droite" :
    			if(j.getPos().getX() < modele.LARGEUR-1 && modele.getZone(j.getPos().getX()+1, j.getPos().getY()).estTraversable()) {
    				j.deplacementDroite(); testVictoire();
    				modele.effectueAction(); 
    			} break;
    			
    			
    		case "AssechHaut" :
    			if(j.getPos().getY() > 0 && modele.getZone(j.getPos().getX(), j.getPos().getY()-1).getEtat() == EtatZone.inondee) {
    				Zone zoneHaut = modele.getZone(j.getPos().getX(),j.getPos().getY()-1);
    				System.out.println("Le joueur "+j.getNom()+" asseche la zone ("+zoneHaut.getX()+","+zoneHaut.getY()+")"); 
    				zoneHaut.assecher(); 
    				modele.effectueAction();;
    			} break;
    			
    			
    		case "AssechBas" :
    			if(j.getPos().getY() < modele.HAUTEUR-1 && modele.getZone(j.getPos().getX(), j.getPos().getY()+1).getEtat() == EtatZone.inondee) {
    				Zone zoneBas = modele.getZone(j.getPos().getX(),j.getPos().getY()+1);
    				System.out.println("Le joueur "+j.getNom()+" asseche la zone ("+zoneBas.getX()+","+zoneBas.getY()+")"); 
    				zoneBas.assecher(); 
    				modele.effectueAction();;
    			} break;
    			
    			
    		case "AssechGauche" :
    			if(j.getPos().getX() > 0 && modele.getZone(j.getPos().getX()-1, j.getPos().getY()).getEtat() == EtatZone.inondee) {
    				Zone zoneGauche = modele.getZone(j.getPos().getX()-1,j.getPos().getY());
    				System.out.println("Le joueur "+j.getNom()+" asseche la zone ("+zoneGauche.getX()+","+zoneGauche.getY()+")"); 
    				zoneGauche.assecher(); 
    				modele.effectueAction();;
    			} break;
    			
    			
    		case "AssechDroite" :
    			if(j.getPos().getX() < modele.LARGEUR && modele.getZone(j.getPos().getX()+1, j.getPos().getY()).getEtat() == EtatZone.inondee) {
    				Zone zoneDroite = modele.getZone(j.getPos().getX()+1,j.getPos().getY());
    				System.out.println("Le joueur "+j.getNom()+" asseche la zone ("+zoneDroite.getX()+","+zoneDroite.getY()+")"); 
    				zoneDroite.assecher(); 
    				modele.effectueAction();;
    			} break;
    			
    			
    		case "AssechIci" :
    			if(j.getPos().getEtat() == EtatZone.inondee) {
    				System.out.println("Le joueur "+j.getNom()+" asseche la zone ("+j.getPos().getX()+","+j.getPos().getY()+")"); 
    				j.getPos().assecher(); 
    				modele.effectueAction();;
    			} break;
    			
    			
    		case "Unlock" :
    			Artefact a = j.getPos().getArtefact();
    			switch (a) {
    			
    			
    				case aucun : ;
    				
    				
    				case feu : if(j.getClesJ().contains(CleArtefact.feu)) {
    					j.useCle(CleArtefact.feu);
    					j.addArtefact(a);
    					System.out.println("Le joueur "+j.getNom()+" recupere l'artefact feu");
    					modele.effectueAction();
    				} break;
    				
    				
    				case air : if(j.getClesJ().contains(CleArtefact.air)) {
    					j.useCle(CleArtefact.air);
    					j.addArtefact(a);
    					System.out.println("Le joueur "+j.getNom()+" recupere l'artefact air");
    					modele.effectueAction();
    				} break;
    				
    				
    				case eau : if(j.getClesJ().contains(CleArtefact.eau)) {
    					j.useCle(CleArtefact.eau);
    					j.addArtefact(a);
    					System.out.println("Le joueur "+j.getNom()+" recupere l'artefact eau");
    					modele.effectueAction();
    				} break;
    				
    				
    				case terre : if(j.getClesJ().contains(CleArtefact.terre)) {
    					j.useCle(CleArtefact.terre);
    					j.addArtefact(a);
    					System.out.println("Le joueur "+j.getNom()+" recupere l'artefact terre");
    					modele.effectueAction();
    				} break;
    				
    			}
    			
    			
    		case "Donner" :
    			Zone p = j.getPos();
    			if(j.getClesJ().size()!=0) {
    				for(int i=0; i<modele.joueurs.size();i++) {
    					if(i!=modele.getJoueurActuel() && modele.joueurs.get(i).getPos()==p) {
    						j.donneCle(modele.joueurs.get(i));
    					}
    				}
    			}
    			
    			
    		case "Passer" :
    			modele.effectueAction();
    		}
    		
    		
    		
    		if(modele.getNbActions()==3) {		// Lorsque le compteur passe à 3 on desactive les boutons d'action et on active le bouton findetour
    			vue.getfinDeTour().setEnabled(true);
        		afficheBoutons(false);
    		}
    	}
    	else {
    	
    	if(e.getActionCommand()=="Tour" && !partieTerminee) {
    		Joueur j = modele.joueurs.get(modele.getJoueurActuel());
			System.out.println("");
			
	    	j.chercheCle();
	    	
    		System.out.println(""); System.out.println("Fin du tour de "+j.getNom());
    		
			modele.inondation();
			
			if(modele.artefactSubmerge) {
				partieTerminee = true;
			}
			
			testNoyade();
			
			testVictoire();
			
			if(!partieTerminee) {
				
				modele.nextPlayer();
				j = modele.joueurs.get(modele.getJoueurActuel());
				
				System.out.println("C'est au tour de "+j.getNom()+", situé sur la case ("+j.getPos().getX()+","+j.getPos().getY()+") de jouer !");
				
				
				for(int i=0; i<j.getClesJ().size();i++) {
					System.out.println(j.getNom()+" possède "+" la cle "+j.getClesJ().get(i));
				}
				
				
				for(int i=0; i<j.getArtefactsJ().size();i++) {
					System.out.println(j.getNom()+" possède "+" l'artefact "+j.getArtefactsJ().get(i));
				}
				
				
				vue.getfinDeTour().setEnabled(false);
				
				afficheBoutons(true);
			}
    	}else { vue.getfinDeTour().setEnabled(false); }
    	
    }
    } public void afficheBoutons(boolean b) {
		vue.getBoutonGauche().setEnabled(b);
    	vue.getBoutonDroite().setEnabled(b);
    	vue.getBoutonHaut().setEnabled(b);
    	vue.getBoutonBas().setEnabled(b);
    	vue.getAssechGauche().setEnabled(b);
    	vue.getAssechDroite().setEnabled(b);
    	vue.getAssechHaut().setEnabled(b);
    	vue.getAssechBas().setEnabled(b);
    	vue.getAssechIci().setEnabled(b);
    	vue.getDeverouiller().setEnabled(b);
    	vue.getEchange().setEnabled(b);
    	vue.getPasser().setEnabled(b);
    	
    }
    public void testNoyade() {
    	for(int i=0; i<modele.joueurs.size();i++) {
    		
			Joueur j = modele.joueurs.get(i);
			
	    	if(j.getPos().getEtat()==EtatZone.submergee) {
	    		
	    		if(j.getPos().getY() < modele.HAUTEUR-1 && modele.getZone(j.getPos().getX(), j.getPos().getY()+1).estTraversable()) {
	    			
					System.out.println("Le joueur "+j.getNom()+" se déplace vers le Bas pour éviter la noyade"); 
					
					j.deplacementBas();
					
					
	    		}else if(j.getPos().getY() > 0 && modele.getZone(j.getPos().getX(), j.getPos().getY()-1).estTraversable()) {
	    			
					System.out.println("Le joueur "+j.getNom()+" se déplace vers le Haut pour éviter la noyade"); 
					
					j.deplacementHaut(); 
					
					
	    		}else if(j.getPos().getX() > 0 && modele.getZone(j.getPos().getX()-1, j.getPos().getY()).estTraversable()) {
	    			
					System.out.println("Le joueur "+j.getNom()+" se déplace vers la Gauche pour éviter la noyade"); 
					
					j.deplacementGauche(); 
					
					
	    		}else if(j.getPos().getX() < modele.LARGEUR-1 && modele.getZone(j.getPos().getX()+1, j.getPos().getY()).estTraversable()) {
	    			
					System.out.println("Le joueur "+j.getNom()+" se déplace vers la Droite pour éviter la noyade"); 
					
					j.deplacementDroite(); 
					
					
	    		}else {
	    			modele.tuerJoueur(i); partieTerminee = true;
	    		}
	    	}
	    }
    }
    public void testVictoire() {
    	boolean joueursSurHeliport = true;
    	
    	for(int i=0; i<modele.joueurs.size();i++) {
    		if(modele.joueurs.get(i).getPos()!=modele.posHeliport) { joueursSurHeliport = false;}
    	}
    	
    	if(modele.artefacts.size()==0 && joueursSurHeliport) {
    		afficheBoutons(false);
    		vue.getfinDeTour().setEnabled(false);
    		System.out.println("Partie gagnée !"); 
    		partieTerminee = true;
    	}
    }
}