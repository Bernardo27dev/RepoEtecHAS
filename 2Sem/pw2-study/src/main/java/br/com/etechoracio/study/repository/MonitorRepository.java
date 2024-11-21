package br.com.etechoracio.study.repository;

import br.com.etechoracio.study.entity.Monitor;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface MonitorRepository extends JpaRepository<Monitor, Long> {

    List<Monitor> findByNomeLike(String nome);
    Monitor findByTelefone(String telefone);
    Monitor findByEmail(String email);
}
