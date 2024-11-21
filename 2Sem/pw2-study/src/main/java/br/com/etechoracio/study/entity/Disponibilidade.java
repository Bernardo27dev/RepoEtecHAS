package br.com.etechoracio.study.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

import java.time.LocalDateTime;

@Getter
@Setter
@Entity
@Table(name = "TBL_DISPONIBILIDADE")
public class Disponibilidade {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "ID_DISPONIBILIDADE")
    private Long id;

    @Column(name = "TX_DIA_SEMANA")
    private String diaSemana;

    @Column(name = "DT_DAS")
    private LocalDateTime das;

    @Column(name = "DT_ATE")
    private LocalDateTime ate;
}
