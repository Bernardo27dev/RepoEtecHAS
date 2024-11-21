package br.com.etechoracio.study.repository;

import br.com.etechoracio.study.entity.Disciplina;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface DisciplinaRepository extends JpaRepository<Disciplina, Long> {

    Optional<Disciplina> findByNomeIgnoreCase(String nome);
}
