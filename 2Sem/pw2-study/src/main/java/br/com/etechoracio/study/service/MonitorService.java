package br.com.etechoracio.study.service;

import br.com.etechoracio.study.entity.Disciplina;
import br.com.etechoracio.study.entity.Monitor;
import br.com.etechoracio.study.repository.DisciplinaRepository;
import br.com.etechoracio.study.repository.MonitorRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class MonitorService {
    @Autowired
    private MonitorRepository repository;

    public Monitor cadastrarMonitor(Monitor monitor){
        var existe = repository.findById(monitor.getId());
        var existingTelefone = repository.findByTelefone(monitor.getWhatsapp());
        var existingEmail = repository.findByEmail(monitor.getEmail());
        if(existe.isEmpty())
            return repository.save(monitor);
        else
            throw new RuntimeException("Nome do monitor já cadastrado");
    }

}
